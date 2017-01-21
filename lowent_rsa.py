from smashcipher.asymmetric import smashrsa

smashrsa.lowentropy("test_keys/lowent/public-lowent1.key",
                    "test_keys/lowent/public-lowent2.key",
                    "test_keys/lowent/private-generated1.key",
                    "test_keys/lowent/private-generated2.key")
