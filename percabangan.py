#makan: str = input("sudah makan belum?: ")
#makan = makan.lower()
#if makan == "belum":
#   print("Silahkan Makan")
#elif makan == "sudah":
#   print("Makannya Banyak")
#else:
#   print("Selamat Makan")


#makan: str = input("sudah makan belum?: ")
#
#match makan:
#    case "sudah":
#        print("Makannya Banyak")
#    case "belum":
#        print("Silahkan Makan")
#    case default:
#        print("apa dong")
#

makan: str = input("sudah makan belum?: ")
makan = makan.lower()   # Convert the makan to lowercase for case-insensitive matching
match makan:
    case "sudah":
        print("Makannya Banyak")
    case "belum":
        print("Silahkan Makan")
    case default:
        print("apa dong")
