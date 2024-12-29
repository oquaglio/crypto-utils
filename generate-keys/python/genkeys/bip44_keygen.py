from bip_utils import (
    Bip39SeedGenerator,
    Bip39MnemonicGenerator,
    Bip39WordsNum,
    Bip44,
    Bip44Coins,
    Bip44Changes
)

def generate_wallet(token_name: str):
    try:
        # Dynamically get the coin from the Bip44Coins enum
        coin = getattr(Bip44Coins, token_name.upper())
    except AttributeError:
        raise ValueError(f"Invalid token name '{token_name}'. Please use a valid Bip44Coins token name.")

    # Generate a new mnemonic (optional)
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
    print(f"Mnemonic Phrase: {mnemonic}")

    # Generate the seed from the mnemonic
    seed = Bip39SeedGenerator(mnemonic).Generate()

    # Create a Bip44 wallet for the given token
    bip44_wallet = Bip44.FromSeed(seed, coin)

    # Get the first account, first change (external addresses), and first address index
    account = bip44_wallet.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)

    # Get the keys and address
    private_key = account.PrivateKey().Raw().ToHex()
    public_key = account.PublicKey().RawCompressed().ToHex()
    address = account.PublicKey().ToAddress()

    print(f"Private Key: {private_key}")
    print(f"Public Key: {public_key}")
    print(f"Address: {address}")

# Example Usage
token_name = input("Enter the token name (e.g., BITCOIN, ETHEREUM, CARDANO): ").strip()
try:
    generate_wallet(token_name)
except ValueError as e:
    print(e)
