import sys
import serial
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class Dashboard(QMainWindow):

    def __init__(self):
        super().__init__()

        self.roll = 0
        self.pitch = 0
        self.yaw = 0

        self.ax = 0
        self.ay = 0
        self.az = 0

        self.gx = 0
        self.gy = 0
        self.gz = 0

        try:
            self.ser = serial.Serial("COM11", 115200, timeout=0.05)
            self.connected = True
        except:
            self.connected = False

        self.init_ui()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(50)

    def init_ui(self):

        self.setWindowTitle("MPU6050 Flight Dashboard")
        self.resize(1400, 850)

        self.setStyleSheet("""
        QMainWindow{
            background:#10141C;
        }

        QLabel{
            color:white;
            font-family:Segoe UI;
        }

        QFrame{
            background:#1B2330;
            border:2px solid #00D4FF;
            border-radius:15px;
        }
        """)

        central = QWidget()
        self.setCentralWidget(central)

        main = QGridLayout()
        central.setLayout(main)

        # Left Panel
        left = QFrame()
        left_layout = QVBoxLayout()

        self.roll_label = QLabel("ROLL\n0°")
        self.pitch_label = QLabel("PITCH\n0°")
        self.yaw_label = QLabel("YAW\n0°")

        for w in [self.roll_label,
                  self.pitch_label,
                  self.yaw_label]:

            w.setAlignment(Qt.AlignmentFlag.AlignCenter)
            w.setStyleSheet("""
            font-size:28px;
            padding:20px;
            """)

            left_layout.addWidget(w)

        left.setLayout(left_layout)

        # Center Aircraft

        center = QFrame()
        center_layout = QVBoxLayout()

        title = QLabel("MPU6050 AIRCRAFT")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setStyleSheet("""
        font-size:32px;
        color:#00D4FF;
        """)

        self.aircraft = QLabel("✈")
        self.aircraft.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.aircraft.setStyleSheet("""
        font-size:180px;
        color:#00D4FF;
        """)

        center_layout.addWidget(title)
        center_layout.addStretch()
        center_layout.addWidget(self.aircraft)
        center_layout.addStretch()

        center.setLayout(center_layout)

        # Right Panel

        right = QFrame()

        right_layout = QVBoxLayout()

        self.accel = QLabel(
            "ACCEL\n\nAX:0\nAY:0\nAZ:0"
        )

        self.gyro = QLabel(
            "GYRO\n\nGX:0\nGY:0\nGZ:0"
        )

        self.status = QLabel(
            "STATUS\nCONNECTED"
            if self.connected
            else "STATUS\nDISCONNECTED"
        )

        for w in [self.accel,
                  self.gyro,
                  self.status]:

            w.setAlignment(Qt.AlignmentFlag.AlignCenter)

            w.setStyleSheet("""
            font-size:24px;
            padding:20px;
            """)

            right_layout.addWidget(w)

        right.setLayout(right_layout)

        main.addWidget(left,0,0)
        main.addWidget(center,0,1)
        main.addWidget(right,0,2)

        main.setColumnStretch(1,2)

    def update_data(self):

        if not self.connected:
            return

        try:

            line = self.ser.readline().decode().strip()

            data = line.split(",")

            if len(data) >= 9:

                self.roll = float(data[0])
                self.pitch = float(data[1])
                self.yaw = float(data[2])

                self.ax = float(data[3])
                self.ay = float(data[4])
                self.az = float(data[5])

                self.gx = float(data[6])
                self.gy = float(data[7])
                self.gz = float(data[8])

                self.roll_label.setText(
                    f"ROLL\n{self.roll:.1f}°"
                )

                self.pitch_label.setText(
                    f"PITCH\n{self.pitch:.1f}°"
                )

                self.yaw_label.setText(
                    f"YAW\n{self.yaw:.1f}°"
                )

                self.accel.setText(
                    f"ACCEL\n\n"
                    f"AX: {self.ax:.2f}\n"
                    f"AY: {self.ay:.2f}\n"
                    f"AZ: {self.az:.2f}"
                )

                self.gyro.setText(
                    f"GYRO\n\n"
                    f"GX: {self.gx:.2f}\n"
                    f"GY: {self.gy:.2f}\n"
                    f"GZ: {self.gz:.2f}"
                )

                transform = QTransform()

                transform.rotate(self.roll)

                pix = QPixmap(300,300)
                pix.fill(Qt.GlobalColor.transparent)

        except:
            pass


app = QApplication(sys.argv)

window = Dashboard()
window.show()

sys.exit(app.exec())