
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;

public class GuessTheNumber {

  public static void main(String[] args) {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    int minNum = 1;
    int maxNum = 1000;
    scanner: {
      for (int i = 0; i < 10; i++) {
        int guessNum = (minNum + maxNum) / 2;
        out.println(guessNum);
        out.flush();
        try {
          switch (in.readLine()) {
          case "lower":
            maxNum = guessNum;
            break;
          case "higher":
            minNum = guessNum + 1;
            break;
          case "correct":
            break scanner;
          }
        } catch (IOException e) {
        }
      }
    }
  }
}
