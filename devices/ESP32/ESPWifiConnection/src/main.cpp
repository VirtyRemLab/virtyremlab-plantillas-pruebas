#include <Arduino.h>
#include <WiFi.h>  
#include <Wire.h>
#include <Pantalla.h>

// put function declarations here:
int myFunction(int, int);
int result = 0;

const char* ssid = "Uniovi-i40";     // Cambia esto por el nombre de tu red WiFi
const char* password = "1000000001"; // Cambia esto por la contraseña de tu red WiFi


void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(115200);
  // Incialización de la pantalla
  Wire.begin(SDA_OLED, SCL_OLED);  
  initOLED(1);

  Serial.println("Conectando a la red WiFi...");

  // Inicia la conexión WiFi
  WiFi.begin(ssid, password);

  // Espera hasta que se conecte
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }


    // Mensaje de éxito
  Serial.println("\n¡Conectado!");
  Serial.print("Dirección IP: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  
  Serial.println(WiFi.localIP());
  
  display.clearDisplay();
  display.setCursor(0, 0); 
  if (WiFi.status() != WL_CONNECTED){
    display.print("Desconectado! \n");
    display.display();
  }
  else{
    display.print("Conectado! \n");
    display.print("IP: "); display.print(WiFi.localIP());
    display.display();
  }           
  


  delay(2000);
}
