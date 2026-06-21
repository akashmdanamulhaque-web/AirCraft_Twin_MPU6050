#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;

float roll = 0;
float pitch = 0;
float yaw = 0;

unsigned long lastTime = 0;

void setup()
{
  Serial.begin(115200);

  Wire.begin(21,22);

  if(!mpu.begin())
  {
    Serial.println("MPU6050 Not Found");
    while(1);
  }

  delay(1000);
}

void loop()
{
  sensors_event_t a, g, temp;

  mpu.getEvent(&a, &g, &temp);

  float ax = a.acceleration.x;
  float ay = a.acceleration.y;
  float az = a.acceleration.z;

  pitch = atan2(ax, sqrt(ay*ay + az*az)) * 180.0 / PI;
  roll  = atan2(ay, sqrt(ax*ax + az*az)) * 180.0 / PI;

  unsigned long now = millis();
  float dt = (now-lastTime)/1000.0;
  lastTime = now;

  yaw += g.gyro.z * dt * 57.2958;

  Serial.print(roll);
  Serial.print(",");

  Serial.print(pitch);
  Serial.print(",");

  Serial.print(yaw);
  Serial.print(",");

  Serial.print(ax);
  Serial.print(",");

  Serial.print(ay);
  Serial.print(",");

  Serial.print(az);
  Serial.print(",");

  Serial.print(g.gyro.x);
  Serial.print(",");

  Serial.print(g.gyro.y);
  Serial.print(",");

  Serial.println(g.gyro.z);

  delay(100);
}