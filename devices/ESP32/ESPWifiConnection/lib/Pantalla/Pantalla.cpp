
#include "Pantalla.h"

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, RST_OLED);

void initOLED(uint8_t textSize)
{

    // Inicializa la pantalla
    if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS))
    {
        
        for (;;);  // Detenerse si falla
  }
  display.display();
  delay(2000);

  display.clearDisplay();
  display.setTextSize(1);             // Tamaño de texto
  display.setTextColor(SSD1306_WHITE);  // Color
  display.println("Ready");
  display.display();
}