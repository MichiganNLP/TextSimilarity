CC = g++
#Using -Ofast instead of -O3 might result in faster code, but is supported only by newer GCC versions
CFLAGS = -lm -pthread -O3 -march=native -Wall -funroll-loops -Wno-unused-result

all: compare

compare : compare.cpp
	$(CC) compare.cpp -o compare $(CFLAGS)

clean:
	rm -rf compare
