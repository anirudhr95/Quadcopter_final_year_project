#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include "I2Cdev.h"
#include "MPU6050.h"
#include "HMC5883L.h"

// class default I2C address is 0x68
// specific I2C addresses may be passed as a parameter here
// AD0 low = 0x68 (default for InvenSense evaluation board)
// AD0 high = 0x69
MPU6050 accelgyro;
HMC5883L magnetom;

int16_t ax, ay, az;
int16_t gx, gy, gz;
int16_t cx, cy, cz;

void setup() {
    // initialize device
    printf("Initializing I2C devices...\n");
    accelgyro.initialize();
    accelgyro.setI2CMasterModeEnabled(0);
    accelgyro.setI2CBypassEnabled(1);
    magnetom.initialize();

    // verify connection
    printf("Testing device connections...\n");
    printf(accelgyro.testConnection() ? "MPU6050 connection successful\n" : "MPU6050 connection failed\n");
    printf(magnetom.testConnection() ? "HMC5883L connection successful\n" : "HMC5883L connection failed\n");
}

void loop() {
    // read raw accel/gyro measurements from device
    accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
    magnetom.getHeading(&cx, &cy, &cz);

    // these methods (and a few others) are also available
    //accelgyro.getAcceleration(&ax, &ay, &az);
    //accelgyro.getRotation(&gx, &gy, &gz);

    // display accel/gyro x/y/z values
    printf("a/g: %6hd %6hd %6hd   %6hd %6hd %6hd %6hd %6hd %6hd\n",ax,ay,az,gx,gy,gz,cx,cy,cz);
}

int main()
{
  setup();
   for (;;)
      loop();
}

