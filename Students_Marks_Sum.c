int marks_summation(int* marks, int number_of_students, char gender) {
  int boys = 0, girls = 0;
  
  for(int i = 0; i < number_of_students; i++){
      if(i % 2) girls += marks[i];
      else boys += marks[i];
  }
  
  return (gender == 'b')?boys:girls;
}
