CC=gcc
SRC=src/main.c src/math_utils.c
OBJ=$(SRC:.c=.o)
OUT=build/main

BUILD ?= release

ifeq ($(BUILD),debug)
    CFLAGS=-Wall -g -DDEBUG
else
    CFLAGS=-Wall -O2 -DNDEBUG
endif

all: $(OUT)

$(OUT): $(OBJ)
	mkdir -p build
	$(CC) $(OBJ) -o $(OUT)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf build
	find src -name '*.o' -delete
