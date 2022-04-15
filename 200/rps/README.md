# rps

### Description

Here's a program that plays rock, paper, scissors against you. 

I hear something good happens if you win 5 times in a row. 

### Resources

- nc saturn.picoctf.net 53296
- game-redacted.c

### Solution

Step 1: Open game-redacted.c in a text editor

Step 2: Notice how the flag is returned in the program

```c
if (wins >= 5) {
  puts("Congrats, here's the flag!");
  puts(flag);
}
```

Step 3: Notice the win condition in the program

```c
if (strstr(player_turn, loses[computer_turn])) {
  puts("You win! Play again?");
  return true;
} else {
  puts("Seems like you didn't win this time. Play again?");return false;
}
```

Step 4: Search for the strstr c function

> returns pointer to the first occurrence of the matched string in the given string

Step 5: Create a test.c program to test the strstr function logic

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int main() {

    char* loses[3] = {"paper", "scissors", "rock"};

    char player_turn[100] = "paperscissorsrock";
    int computer_turn = rand() % 3;
    printf("player_turn: %s\n", player_turn);
    printf("loses[computer_turn]: %s\n", loses[computer_turn]);

    if (strstr(player_turn, loses[computer_turn])) {
        puts("You win! Play again?");
        return true;
    } else {
        puts("Seems like you didn't win this time. Play again?");
        return false;
    }
    return 0;
}
```

Step 6: Connect to pico nc 

Step 7: Use the tested answer

And FLAGTIME :exclamation: :exclamation: