import javax.swing.JOptionPane;

public class Grades
{
	public static void main(String[] args)
	{
		String origLetter = JOptionPane.showInputDialog("Please enter Letter Grade:");
    
		String origNumeric = JOptionPane.showInputDialog("Please enter Numeric Grade:");

		//constructor of new Grade object from Grade.java file
		Grade userGrades = new Grade(origLetter, Double.parseDouble(origNumeric));
    
    //displays the final result
		
		JOptionPane.showMessageDialog(null,
				"Numeric Grade Equivalent = " + userGrades.getNewNumeric() +
						"\n\nLetter Grade Equivalent = " + userGrades.getNewLetter(),
				"Grades",
				JOptionPane.INFORMATION_MESSAGE);
	}
}