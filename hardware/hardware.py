import serial,time,threading

class BrailleEncoder:

    __braille_dict = {
            "a": "000000100000",
            "b": "000000101000",
            "c": "000000110000",
            "d": "000000110100",
            "e": "000000100100",
            "f": "000000111000",
            "g": "000000111100",
            "h": "000000101100",
            "i": "000000011000",
            "j": "000000011100",
            "k": "000000100010",
            "l": "000000101010",
            "m": "000000110010",
            "n": "000000110110",
            "o": "000000100110",
            "p": "000000111010",
            "q": "000000111110",
            "r": "000000101110",
            "s": "000000011010",
            "t": "000000011110",
            "u": "000000100011",
            "v": "000000101011",
            "w": "000000011101",
            "x": "000000110011",
            "y": "000000110111",
            "z": "000000100111",
            "ñ": "000000111101",
            "á": "000000101111",
            "é": "000000011011",
            "í": "000000010010",
            "ó": "000000010011",
            "ú": "000000011111",
            "A": "010001100000",
            "B": "010001101000",
            "C": "010001110000",
            "D": "010001110100",
            "E": "010001100100",
            "F": "010001111000",
            "G": "010001111100",
            "H": "010001101100",
            "I": "010001011000",
            "J": "010001011100",
            "K": "010001100010",
            "L": "010001101010",
            "M": "010001110010",
            "N": "010001110110",
            "O": "010001100110",
            "P": "010001111010",
            "Q": "010001111110",
            "R": "010001101110",
            "S": "010001011010",
            "T": "010001011110",
            "U": "010001100011",
            "V": "010001101011",
            "W": "010001011101",
            "X": "010001110011",
            "Y": "010001110111",
            "Z": "010001100111",
            "Ñ": "010001111101",
            "Á": "010001101111",
            "É": "010001011011",
            "Í": "010001010010",
            "Ó": "010001010011",
            "Ú": "010001011111",
            ".": "000000000010",
            ",": "000000001000",
            ";": "000000001010",
            ":": "000000001100",
            "_": "000000000011",
            "'": "000000001011",
            "!": "000000001110",
            "¡": "000000001110",
            "?": "000000001001",
            "¿": "000000001001",
            "(": "000000101001",
            ")": "000000010110",
            "[": "000000101001",
            "]": "000000010110",
            "{": "000000101001",
            "}": "000000010110",
            "+": "000000001110",
            "*": "000000000110",
            "=": "000000001111",
            "/": "000000001101",
            "-": "000000000011",
            "1": "010111100000",
            "2": "010111101000",
            "3": "010111110000",
            "4": "010111110100",
            "5": "010111100100",
            "6": "010111111000",
            "7": "010111111100",
            "8": "010111101100",
            "9": "010111011000",
            "0": "010111011100",
            " ": "000000000000"
        }

    __special_chars = ["ñ","ü","á","é","í","ó","ú","Ñ","Ü","Á","É","Í","Ó",
                        "Ú","¿","¡","\"","'"]
    
    
    def __init__(self,message="",directly=False,ard=None):
        if directly:
            if ard is not None:
                self.sequence = ard
            else:
                raise ValueError("If 'directly' is set to True, 'ard' must be provided.")
        else:
            self.message = message + " "
            self.sequence = [(self.__braille_dict[char] + char) for char in self.message]
        self.pos = 0  
        self.finished = False
        
    def next(self):
        if self.pos < len(self.sequence) - 1:
            self.pos += 1
        else:
            self.sequence = ["000000000000 "]
            self.pos = 0
            self.finished = True
    
    def get_character(self):
        return (self.sequence[self.pos]).encode("ascii")



class Hardware:
    def __init__(self, port="COM3", baudrate=9600):
        self.ser = serial.Serial(port, baudrate)
        self.thread = threading.Thread(target=self.listen)
        self.encoder = None
        self.wait_time = 2

    def listen(self):
        while True:
            if self.ser.inWaiting():
                message = self.ser.readline().decode('utf-8').rstrip()
                if message == "next":
                    time.sleep(self.wait_time)
                    self.ser.write(self.encoder.get_character())
                    print("It's reviced ", self.encoder.get_character())
                    self.encoder.next()
                    if self.encoder.finished:
                        break 

    def send(self,message="",directly=False,ard=None):
        if self.encoder is not None:
            raise Exception("There is already a message being encoded")
        if directly:
            print("directly")
            if ard is not None:
                self.encoder = BrailleEncoder(message,directly=True,ard=ard)
            else:
                raise ValueError("If 'directly' is set to True, 'ard' must be provided.")
        else:
            self.encoder = BrailleEncoder(message)
 
    def close(self):
        self.ser.close()

# Crea la instancia de Hardware
hardware = Hardware()

# Configura el encoder y comienza a escuchar
hardware.send("Hello word")

print("Waiting for the message to be sent")
# Espera hasta que termine la codificacion
while not hardware.encoder.finished:
    time.sleep(1)  # Espera un segundo para evitar sobrecargar la CPU

# Cierra la conexion
hardware.close()

print("Finished")
