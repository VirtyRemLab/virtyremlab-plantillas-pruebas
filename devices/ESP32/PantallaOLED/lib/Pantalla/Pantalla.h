#ifndef PANTALLA_H
#define PANTALLA_H


#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>


#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1  // Reset no está conectado
#define SCREEN_ADDRESS 0x3C  // Dirección I2C común para esta pantalla
extern Adafruit_SSD1306 display;


// Función para inicializar la pantalla
void initOLED(uint8_t textSize);

#endif