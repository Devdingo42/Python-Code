public class Grade
{
	  // Instance fields
      private String origLetter;
      private double newNumeric;
      
      private double origNumeric;
      private String newLetter;
      
      // Default constructor
      public Grade()
      {
          origLetter = "";
          origNumeric = 0;
          newLetter = "";
          newNumeric = 0;
      }
      
      // Parametric constructor
      public Grade(String oldLetter, double oldNumeric)
      {
          origLetter = oldLetter;
          origNumeric = oldNumeric;
          
          setNewNumeric();
          setNewLetter();
      }
      
      // Mutator method for new numeric grade
      private void setNewNumeric()
      {
          if (origLetter.substring(0, 1).equals("A"))
          {
              newNumeric = 4;
          }
          else if (origLetter.substring(0, 1).equals("B")){
              newNumeric = 3;
          }
          else if (origLetter.substring(0, 1).equals("C")){
              newNumeric = 2;
          }
      else if (origLetter.substring(0, 1).equals("D")) {
          newNumeric = 1;
      } 
      else {
          newNumeric = 0;
      }
          }
          
        //Complete the other cases
      
      // Mutator method for new letter grade
      private void setNewLetter()
      {
          if (origNumeric == 4)
          {
              newLetter = "A+";
          }
          else if (origNumeric <= 3.99 && origNumeric >= 3.85)
          {
              newLetter = "A";
          }
          else if (origNumeric >= 3.5) {
              newLetter = "B";
          } 
          else if (origNumeric >= 2.5) {
              newLetter = "C";
          } 
          else if (origNumeric >= 1.5) {
              newLetter = "D";
          } 
          else {
              newLetter = "F";
          }
      }
  
            //Complete the other cases
      
      // Accessor method for new numeric grade
      public double getNewNumeric()
      {
          return newNumeric;
      }
      
      // Accessor method for new letter grade
      public String getNewLetter()
      {
          return newLetter;
      }
}