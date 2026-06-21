from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight
import serial
import threading


class AircraftViewer(ShowBase):

    def __init__(self):
        super().__init__()

        self.disableMouse()
        self.setBackgroundColor(0, 0, 0, 1)

        # Camera
        self.camera.setPos(0, -100, 25)
        self.camera.lookAt(0, 0, 0)

        # MPU values
        self.roll = 0
        self.pitch = 0
        self.yaw = 0

        # Root node (receives MPU rotations)
        self.aircraft_root = self.render.attachNewNode("aircraft_root")

        # Load aircraft model
        self.aircraft = self.loader.loadModel("Jet.glb")
        self.aircraft.reparentTo(self.aircraft_root)

        # Scale
        self.aircraft.setScale(3)

        # MODEL ORIENTATION FIX
        # Try these values if aircraft is not level:
        self.aircraft.setHpr(0, 90, 90)

        # Lights
        ambient = AmbientLight("ambient")
        ambient.setColor((0.8, 0.8, 0.8, 1))
        self.render.setLight(self.render.attachNewNode(ambient))

        sun = DirectionalLight("sun")
        sun.setColor((1, 1, 1, 1))
        sun_np = self.render.attachNewNode(sun)
        sun_np.setHpr(-45, -45, 0)
        self.render.setLight(sun_np)

        # Serial
        self.ser = serial.Serial(
            "COM11",
            115200,
            timeout=0.05
        )

        threading.Thread(
            target=self.read_serial,
            daemon=True
        ).start()

        self.taskMgr.add(
            self.update_aircraft,
            "update_aircraft"
        )

    def read_serial(self):

        while True:

            try:
                line = self.ser.readline().decode().strip()

                if not line:
                    continue

                data = line.split(",")

                if len(data) >= 3:

                    self.roll = float(data[0])
                    self.pitch = float(data[1])
                    self.yaw = float(data[2])

            except Exception as e:
                print("Serial Error:", e)

    def update_aircraft(self, task):

        # Uncomment to see values
        # print(self.roll, self.pitch, self.yaw)

        self.aircraft_root.setR(self.roll)
        self.aircraft_root.setP(self.pitch)
        self.aircraft_root.setH(self.yaw)

        return task.cont


app = AircraftViewer()
app.run()