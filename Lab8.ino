#include <DHT.h>

#define DHTPIN 10  // Pin al que está conectado el sensor DHT11
#define DHTTYPE DHT11  // Tipo de sensor DHT (DHT11 para este caso)

DHT dht(DHTPIN, DHTTYPE);

// Definición de pines para los segmentos del display (Ánodo común)
int segmentA = 2;
int segmentB = 3;
int segmentC = 4;
int segmentD = 5;
int segmentE = 6;
int segmentF = 7;
int segmentG = 8;
const int puntoDecimal = 9; // Pin para el punto decimal

// Definir pines para cada segmento del display
const int segmentos[] = {segmentA, segmentB, segmentC, segmentD, segmentE, segmentF, segmentG};

// Definir los patrones para cada número (0-9)
const byte numeros[10][7] = {
  {1, 1, 1, 1, 1, 1, 0}, // 0
  {0, 1, 1, 0, 0, 0, 0}, // 1
  {1, 1, 0, 1, 1, 0, 1}, // 2
  {1, 1, 1, 1, 0, 0, 1}, // 3
  {0, 1, 1, 0, 0, 1, 1}, // 4
  {1, 0, 1, 1, 0, 1, 1}, // 5
  {1, 0, 1, 1, 1, 1, 1}, // 6
  {1, 1, 1, 0, 0, 0, 0}, // 7
  {1, 1, 1, 1, 1, 1, 1}, // 8
  {1, 1, 1, 1, 0, 1, 1}  // 9
};

void setup() {
  Serial.begin(9600);
  dht.begin();  // Inicializar el sensor DHT11

  // Configurar los pines de los segmentos como salida
  for (int i = 0; i < 7; i++) {
    pinMode(segmentos[i], OUTPUT);
  }
  
  // Configurar el pin del punto decimal como salida
  pinMode(puntoDecimal, OUTPUT);
}

void loop() {
  delay(1000);  // Esperar 1 segundo entre cada lectura

  // Leer la humedad relativa
  float humedad = dht.readHumidity();
  
  // Leer la temperatura en grados Celsius
  float temperatura = dht.readTemperature();

  // Verificar si la lectura de temperatura es válida
  if (isnan(humedad) || isnan(temperatura)) {
    Serial.println("Error al leer el sensor DHT11");
    return;
  }

  // Imprimir la lectura de humedad y temperatura en el Monitor Serie
  Serial.print("Humedad: ");
  Serial.print(humedad);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" °C");

  // Mostrar números del 1 al 9 en el display con punto decimal intermitente
  for (int numero = 1; numero <= 9; numero++) {
    mostrarNumero(numero);
    delay(2000); // Esperar 2 segundos entre cada número
  }
}

void mostrarNumero(int numero) {
  // Apagar todos los segmentos y el punto decimal
  for (int i = 0; i < 7; i++) {
    digitalWrite(segmentos[i], HIGH); // Apagar segmento (HIGH en ánodo común)
  }
  digitalWrite(puntoDecimal, HIGH); // Apagar el punto decimal
  
  // Encender los segmentos correspondientes al número
  for (int i = 0; i < 7; i++) {
    digitalWrite(segmentos[i], numeros[numero][i]); // Encender segmento según el patrón
  }
}


























