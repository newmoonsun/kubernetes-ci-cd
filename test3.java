import java.lang.Math;


class Main {
  public static void main(String[] args) {

    // create int variable
    int a = 5;
    int b = 6;

    // multiplyExact() with int arguments
    System.out.println(Math.multiplyExact(a, b));  // 30

    // create long variable
    long c = 7236L;
    long d = 1721L;

    // multiplyExact() with long arguments
    System.out.println(Math.multiplyExact(c, d));  // 12453156
  }
}

public class SwapNumbers {

    public static void main(String[] args) {

        float first = 1.20f, second = 2.45f;

        System.out.println("--Before swap--");
        System.out.println("First number = " + first);
        System.out.println("Second number = " + second);

        // Value of first is assigned to temporary
        float temporary = first;

        // Value of second is assigned to first
        first = second;

        // Value of temporary (which contains the initial value of first) is assigned to second
        second = temporary;

        System.out.println("--After swap--");
        System.out.println("First number = " + first);
        System.out.println("Second number = " + second);
    }
}

