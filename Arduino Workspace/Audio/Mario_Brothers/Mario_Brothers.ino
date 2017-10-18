const unsigned int notes [12] = {
  //C, C#, D, D#, E, F, F#, G, G#, A, A#, B
  262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494
};

const unsigned int beatLength = 1000 / 6;

void playNote ( byte pin, char note, byte octave = 4, bool isSharp = false) {
  bool lowerCase = true;
  bool valid = false;
  {
    if ( 'a' <= note && 'g' >= note) {
      valid = true;
      lowerCase = true;
    } else if ( 'A' <= note && 'G' >= note) {
      lowerCase = false;
      valid = true;
    } else {
      valid = false;
    }
  }
  if (valid) {
    byte index = 0;
    switch (note) {
      case 'c':
      case 'C': {
          if (isSharp) {
            index = 1;
          } else {
            index = 0;
          }
        }
        break;
      case 'd':
      case 'D': {
          if (isSharp) {
            index = 3;
          } else {
            index = 2;
          }
        }
        break;
      case 'e':
      case 'E': {
          index = 4;
        }
        break;
      case 'f':
      case 'F': {
          if (isSharp) {
            index = 6;
          } else {
            index = 5;
          }
        }
        break;
      case 'g':
      case 'G': {
          if (isSharp) {
            index = 8;
          } else {
            index = 7;
          }
        }
        break;
      case 'a':
      case 'A': {
          if (isSharp) {
            index = 10;
          } else {
            index = 9;
          }
        }
        break;
      default:
        index = 11;
    }
    unsigned int frequency = notes [index] * pow(2, octave - 4);

    tone (pin, 2 * frequency);
  }
}
void playNoteTimed(byte pin, double beats, char note, byte octave = 4, bool isSharp = false) {
  noTone(pin);
  delay(1);
  playNote(pin, note, octave, isSharp);
  delay(beatLength * beats);
}



void setup() {
  //Intro

  playNoteTimed(6, 1, 'e');
  playNoteTimed(6, 1, 'e');
  playNoteTimed(6, 1, 'r');
  playNoteTimed(6, 1, 'e');
  playNoteTimed(6, 1, 'r');
  playNoteTimed(6, 1, 'c');
  playNoteTimed(6, 1, 'e');
  playNoteTimed(6, 1, 'r');
  playNoteTimed(6, 1, 'g');
  playNoteTimed(6, 3, 'r');
  playNoteTimed(6, 1, 'g', 3);
  playNoteTimed(6, 3, 'r');

  //Main Loop
  playNoteTimed(6, 1, 'c');
  playNoteTimed(6, 2, 'r');
  playNoteTimed(6, 1, 'g', 3);
  playNoteTimed(6, 2, 'r', 3);
  playNoteTimed(6, 1, 'e', 3);
  playNoteTimed(6, 2, 'r', 3);
  playNoteTimed(6, 1, 'a', 3);
  playNoteTimed(6, 1, 'r', 3);
  playNoteTimed(6, 1, 'b', 3);
  playNoteTimed(6, 1, 'r', 3);
  playNoteTimed(6, 1, 'a', 3, true);
  playNoteTimed(6, 1, 'a', 3);
  playNoteTimed(6, 1, 'r', 3);

  playNoteTimed(6, 4 / 3, 'g', 3);
  playNoteTimed(6, 4 / 3, 'e', 4);
  playNoteTimed(6, 4 / 3, 'g', 4);
  playNoteTimed(6, 1, 'a', 4);
  playNoteTimed(6, 1, 'r', 3);
  playNoteTimed(6, 1, 'f', 4);
  playNoteTimed(6, 1, 'g', 4);
  playNoteTimed(6, 1, 'r', 3);
  playNoteTimed(6, 1, 'e', 4);
  playNoteTimed(6, 1, 'r', 3);
  playNoteTimed(6, 1, 'c', 4);
  playNoteTimed(6, 1, 'd', 4);
  playNoteTimed(6, 1, 'b', 3);
  playNoteTimed(6, 2, 'r', 4);

  playNoteTimed(6, 1, 'c');
  playNoteTimed(6, 2, 'r');
  playNoteTimed(6, 1, 'g', 3);
  playNoteTimed(6, 2, 'r', 3);
  playNoteTimed(6, 1, 'e', 3);
  playNoteTimed(6, 2, 'r', 3);
  playNoteTimed(6, 1, 'a', 3);
  playNoteTimed(6, 1, 'r', 3);
  playNoteTimed(6, 1, 'b', 3);
  playNoteTimed(6, 1, 'r', 3);
  playNoteTimed(6, 1, 'a', 3, true);
  playNoteTimed(6, 1, 'a', 3);
  playNoteTimed(6, 1, 'r', 3);

  playNoteTimed(6, 4 / 3, 'g', 3);
  playNoteTimed(6, 4 / 3, 'e', 4);
  playNoteTimed(6, 4 / 3, 'g', 4);
  playNoteTimed(6, 1, 'a', 4);
  playNoteTimed(6, 1, 'r', 3);
  playNoteTimed(6, 1, 'f', 4);
  playNoteTimed(6, 1, 'g', 4);
  playNoteTimed(6, 1, 'r', 3);
  playNoteTimed(6, 1, 'e', 4);
  playNoteTimed(6, 1, 'r', 3);
  playNoteTimed(6, 1, 'c', 4);
  playNoteTimed(6, 1, 'd', 4);
  playNoteTimed(6, 1, 'b', 3);
  playNoteTimed(6, 2, 'r', 4);

  playNoteTimed(6, 2, 'r', 4);
  playNoteTimed(6, 1, 'g', 4);
  playNoteTimed(6, 1, 'f', 4, true);
  playNoteTimed(6, 1, 'f', 4);
  playNoteTimed(6, 1, 'd', 4, true);
  playNoteTimed(6, 1, 'r', 4);
  playNoteTimed(6, 1, 'e', 4);
  playNoteTimed(6, 1, 'r', 4);
  playNoteTimed(6, 1, 'g', 3, true);
  playNoteTimed(6, 1, 'a', 3);
  playNoteTimed(6, 1, 'c', 4);
  playNoteTimed(6, 1, 'r', 3);
  playNoteTimed(6, 1, 'a', 3);
  playNoteTimed(6, 1, 'c', 4);
  playNoteTimed(6, 1, 'd', 4);

  playNoteTimed(6, 2, 'r', 3);
  playNoteTimed(6, 1, 'g', 4);
  playNoteTimed(6, 1, 'f', 4, true);
  playNoteTimed(6, 1, 'f', 4);
  playNoteTimed(6, 1, 'd', 4, true);
  playNoteTimed(6, 1, 'r', 3);
  playNoteTimed(6, 1, 'e', 4);
  playNoteTimed(6, 1, 'r', 4);
  playNoteTimed(6, 1, 'c', 5);
  playNoteTimed(6, 1, 'r', 4);
  playNoteTimed(6, 1, 'c', 5);
  playNoteTimed(6, 1, 'c', 5);
  playNoteTimed(6, 3, 'r');

  playNoteTimed(6, 2, 'r', 4);
  playNoteTimed(6, 1, 'g', 4);
  playNoteTimed(6, 1, 'f', 4, true);
  playNoteTimed(6, 1, 'f', 4);
  playNoteTimed(6, 1, 'd', 4, true);
  playNoteTimed(6, 1, 'r', 4);
  playNoteTimed(6, 1, 'e', 4);
  playNoteTimed(6, 1, 'r', 4);
  playNoteTimed(6, 1, 'g', 3, true);
  playNoteTimed(6, 1, 'a', 3);
  playNoteTimed(6, 1, 'c', 4);
  playNoteTimed(6, 1, 'r', 3);
  playNoteTimed(6, 1, 'a', 3);
  playNoteTimed(6, 1, 'c', 4);
  playNoteTimed(6, 1, 'd', 4);

  playNoteTimed(6, 1.5, 'r', 4);
  playNoteTimed(6, 1.5, 'd', 4, true);
  playNoteTimed(6, 1.5, 'r', 4);
  playNoteTimed(6, 1.5, 'd', 4);
  playNoteTimed(6, 1, 'r', 4);
  playNoteTimed(6, 1.5, 'c', 4);
  playNoteTimed(6, 1.75, 'r', 4);
  playNoteTimed(6, 1, 'g', 4);
  playNoteTimed(6, 1, 'g', 4);
  playNoteTimed(6, .75, 'r', 4);
  playNoteTimed(6, 1.25, 'c', 4);
  playNoteTimed(6, 2.75, 'r', 4);
}

void loop() {
  noTone(6);
}
