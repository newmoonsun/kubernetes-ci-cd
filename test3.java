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