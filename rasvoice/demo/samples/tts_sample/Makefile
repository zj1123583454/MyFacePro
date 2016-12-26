#common makefile header

DIR_INC = ../../include
DIR_BIN = ../../bin
DIR_LIB = ../../libs

TARGET	= tts_sample.so
BIN_TARGET = $(DIR_BIN)/$(TARGET)

CROSS_COMPILE = 
CFLAGS = -g -Wall -I$(DIR_INC)

#可根据实际需要修改，选择所需平台SDK，默认为x64或x86平台。
ifdef LINUX64
LDFLAGS := -L$(DIR_LIB)/x64
else
LDFLAGS := -L$(DIR_LIB)/x64
endif
LDFLAGS += -lmsc -lrt -ldl -lpthread -shared -fPIC

OBJECTS := $(patsubst %.c,%.o,$(wildcard *.c))

#$(CROSS_COMPILE)gcc $(CFLAGS) $^ -o $@ $(LDFLAGS)

$(BIN_TARGET) : $(OBJECTS)
	gcc -o libtts_sample.so $(CFLAGS) -shared -fPIC tts_sample.c $(LDFLAGS)

%.o : %.c
	$(CROSS_COMPILE)gcc -c $(CFLAGS) $< -o $@
clean:
	@rm -f *.o $(BIN_TARGET)

.PHONY:clean

#common makefile foot
