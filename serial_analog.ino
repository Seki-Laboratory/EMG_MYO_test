const int val_size = 5;
char data;
int val1 = 0;
int val2 = 0;
int val3 = 0;
int val4 = 0;
int val5 = 0;


void setup(){
  Serial.begin(115200);
}

void loop(){  


  if(Serial.available()> 0){

  val1=analogRead(0);
  val2=analogRead(1);
  val3=analogRead(2);
  val4=analogRead(3);
  val5=analogRead(4);



   String s1 = String(val1);
  String s2 = String(val2);
  String s3 = String(val3);
  String s4 = String(val4);
  String s5 = String(val5);
  String s = ",";

  Serial.println(s1+s+s2+s+s3+s+s4+s+s5);
  delay(5);
  
  }
  
}