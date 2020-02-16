import javax.swing.*;
class hello{
    public static void main(String args[]){
       JFrame frame = new JFrame("My First GUI");
       frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       frame.setSize(500,300);
       Icon icon = new ImageIcon("cabbarOysh112.png");
       JButton button = new JButton("YASOOOO MOOOONNTTTTT",icon);
       frame.setLocationRelativeTo(null);
       frame.getContentPane().add(button); // Adds Button to content pane of frame
       frame.setVisible(true);
       button.addActionListener(e -> {
        frame.dispose();
     });
    }
}

