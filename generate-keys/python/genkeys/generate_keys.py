from bip_utils import Bip39SeedGenerator, Bip39MnemonicGenerator, Bip39WordsNum, Bip44, Bip44Coins, Bip44Changes

# Generate a new mnemonic (optional)
mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_24)
print(f"Mnemonic Phrase: {mnemonic}")

# Generate the seed from the mnemonic
seed = Bip39SeedGenerator(mnemonic).Generate()

# Create a Bip44 wallet (e.g., Bitcoin as default example)
bip44_wallet = Bip44.FromSeed(seed, Bip44Coins.BITCOIN)

# Get the first account, first change (external addresses), and first address index
account = bip44_wallet.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)

# Get the keys and address
private_key = account.PrivateKey().Raw().ToHex()
public_key = account.PublicKey().RawCompressed().ToHex()
address = account.PublicKey().ToAddress()

print(f"Private Key: {private_key}")
print(f"Public Key: {public_key}")
print(f"Address: {address}")