String readString;
String startstring,bpval, bp1,bp2,outputbp;
String val, v1, v2, output;
String tstring,ninject_index1,ninject_index2,ninjectstring;
String pulsewidth_index1, pulsewidth_index2, pulsewidthstring;
int bpvolt,apv, ninject,pulsewidth,n; //backpressure volt,inject pressure volt,num inject,pulsewidth of inject, conuter


void setup() {
  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(2, OUTPUT);
  
}

void loop() {
 //runs when no data is here
 
 
  while (!Serial.available()) {
    } 

  //when something is being sent... buffer is 30ms
  while (Serial.available()) {
    delay(30);
    char c = Serial.read();
    readString += c;
    Serial.println("yo");

  }
    
  //delay(100);
  //clear strings
  readString = "";
  

  Serial.println("yooo");
}
