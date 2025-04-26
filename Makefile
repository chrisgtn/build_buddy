CC = gcc
SRCS = src/main.c src/sound_utils.c
OBJS = $(patsubst src/%.c,build/%.o,$(SRCS))
OUT = build/main

BUILD ?= release

ifeq ($(BUILD),debug)
    CFLAGS = -Wall -g -DDEBUG
else
    CFLAGS = -Wall -O2 -DNDEBUG
endif

all: $(OUT)

$(OUT): $(OBJS)
	mkdir -p build
	$(CC) $(CFLAGS) $(OBJS) -o $(OUT)

build/%.o: src/%.c
	mkdir -p build
	$(CC) $(CFLAGS) -c $< -o $@

.PHONY: clean
clean:
	rm -rf build

