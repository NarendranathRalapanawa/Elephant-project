// Define pin for ADC input
const int adcPin = A0;

// Variable to store ADC result
volatile int adcResult = 0;

// Timer configuration parameters
const long samplingRate = 1000; // Sampling rate in Hz (e.g., 1000 Hz)

// ISR for ADC conversion complete
ISR(ADC_vect) {
  adcResult = ADC; // Read the ADC result (10-bit value)
}

// ISR for Timer1 Compare Match
ISR(TIMER1_COMPA_vect) {
  // Start an ADC conversion
  ADCSRA |= (1 << ADSC); // Set the Start Conversion bit
}

void setup() {
  // Initialize serial communication for debugging
  Serial.begin(9600);

  // Configure ADC
  ADMUX = (1 << REFS0) | (adcPin & 0x07); // AVcc as reference, select adcPin 0x07 is use for ensure it will not exceed 3 bits
  ADCSRA = (1 << ADEN)  | // Enable ADC
           (1 << ADIE)  | // Enable ADC interrupt
           (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0); // Prescaler = 128
  
  // Configure Timer1
  cli(); // Disable interrupts during configuration
  TCCR1A = 0; // Clear Timer1 control register A
  TCCR1B = (1 << WGM12) | (1 << CS11); // CTC mode, Prescaler = 8
  OCR1A = (16000000 / (8 * samplingRate)) - 1; // Set compare match value
  TIMSK1 = (1 << OCIE1A); // Enable Timer1 Compare A interrupt
  sei(); // Enable global interrupts
}

void loop() {
  // Main code (optional) - You can process the ADC result here
  Serial.println(adcResult); // Print the ADC result
  delay(100); // For demonstration, print every 100 ms
}
