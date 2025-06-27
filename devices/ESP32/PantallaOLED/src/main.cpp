#include <Arduino.h>
#include <Wire.h>
#include <Pantalla.h>


void setup() {
  // Inicializa comunicación I2C con pines personalizados (opcional)
  Wire.begin(SDA_OLED, SCL_OLED);  
  initOLED(1);
  // put your setup code here, to run once:
  Serial.begin(115200);


}

void loop() {
  
  display.clearDisplay();
  display.setCursor(0, 0);            
  display.print("Hola desde ESP32! \n");
  display.print("Segunda linea");
  display.display();
  Serial.println("Hola");
  // delay(2000)
}
