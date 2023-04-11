package main
import (
	"fmt"
	"math/rand"
	"strconv"
	"os"
)

func main() {
	fmt.Println("\033[1mNumber Guessing Game\033[0m\n")
	min, max := 1, 10
	randnum := rand.Intn(max-1) + 1;
	tries := 15;
	for i:=0; i < 10; i++ {
		fmt.Printf("Guess a random number between %d and %d.\n", min, max);
		guessstr := "";
		fmt.Print("Guess: ");
		fmt.Scanln(&guessstr);
		randnumstr := strconv.Itoa(randnum);

		if randnumstr == guessstr {
			fmt.Printf("You guessed correctly! The number was %d.\n\n", randnum)
			max += 5;
			randnum = rand.Intn(max-1) + 1;
		} else {
			tries--;
			i--;
			if tries <= 0 {
				fmt.Printf("You ran out of attempts. The number was %d.\n", randnum);
				os.Exit(0)
			} else {
				fmt.Printf("You guessed incorrectly. Try again. You have %d tries left.\n\n", tries);
			};
		};
	};
}
