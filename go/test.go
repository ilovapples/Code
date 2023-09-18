package main
import ("fmt")

func test() {
	num1 := 5;
	num2 := 8;
	num3 := 15;
	num4 := 108;

	fmt.Printf("%-4d", num1); fmt.Printf("%4d\n", num1);
	fmt.Printf("%-4d", num2); fmt.Printf("%4d\n", num2);
	fmt.Printf("%-4d", num3); fmt.Printf("%4d\n", num3);
	fmt.Printf("%-4d", num4); fmt.Printf("%4d\n", num4);
}