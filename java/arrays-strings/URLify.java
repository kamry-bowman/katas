public class URLify {

  private static int first_char(char[] string, int count) {
    for (int index = count - 1; index >= 0; index--) {
      if (string[index] == ' ') {
        continue;
      }
      return index;
    }
    return -1;
  }

  private static int add_space(char[] string, int index) {
    string[index] = '0';
    string[index - 1] = '2';
    string[index - 2] = '%';

    return index - 3;
  }

  public static void solve(char[] string, int count) {
    int source_pointer = first_char(string, count);
    int target_pointer = count - 1;

    while (source_pointer < target_pointer) {
      if (string[source_pointer] == ' ') {
        target_pointer = add_space(string, target_pointer);
        source_pointer -= 1;
      } else {
        string[target_pointer] = string[source_pointer];
        source_pointer -= 1;
        target_pointer -= 1;
      }
    }
  }

  public static void main(String[] args) {
    String string = "Mr John Smith    ";
    char[] solution = string.toCharArray();
    solve(solution, string.length());
    System.out.println(new String(solution));
  }
}
