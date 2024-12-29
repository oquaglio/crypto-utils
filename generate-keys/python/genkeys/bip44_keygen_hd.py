from bip_utils import (
    Bip39SeedGenerator,
    Bip39MnemonicGenerator,
    Bip39WordsNum,
    Bip44,
    Bip44Coins,
    Bip44Changes
)

def generate_hd_wallet_addresses(token_name: str, num_addresses: int = 5):
    try:
        # Dynamically get the coin from the Bip44Coins enum
        coin = getattr(Bip44Coins, token_name.upper())
    except AttributeError:
        raise ValueError(f"Invalid token name '{token_name}'. Please use a valid Bip44Coins token name.")

    # Generate a new mnemonic
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
    print(f"Mnemonic Phrase: {mnemonic}\n")

    # Generate the seed from the mnemonic
    seed = Bip39SeedGenerator(mnemonic).Generate()

    # Create a Bip44 wallet for the given token
    bip44_wallet = Bip44.FromSeed(seed, coin)

    # Display the master keys
    master_private_key = bip44_wallet.PrivateKey().Raw().ToHex()
    master_public_key = bip44_wallet.PublicKey().RawCompressed().ToHex()
    print(f"Master Private Key: {master_private_key}")
    print(f"Master Public Key: {master_public_key}")
    print("\nGenerated Addresses:\n" + "-" * 40)

    # Generate multiple addresses
    for index in range(num_addresses):
        # Derive the account, change type, and address index
        account = bip44_wallet.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(index)

        # Extract private key, public key, and address
        private_key = account.PrivateKey().Raw().ToHex()
        public_key = account.PublicKey().RawCompressed().ToHex()
        address = account.PublicKey().ToAddress()

        print(f"Address Index: {index}")
        print(f"Private Key: {private_key}")
        print(f"Public Key: {public_key}")
        print(f"Address: {address}")
        print("-" * 40)

# Example Usage
token_name = input("Enter the token name (e.g., BITCOIN, ETHEREUM, CARDANO): ").strip()
num_addresses = int(input("Enter the number of addresses to generate: "))
try:
    generate_hd_wallet_addresses(token_name, num_addresses)
except ValueError as e:
    print(e)
