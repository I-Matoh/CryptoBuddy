# CryptoBuddy: Your First AI-Powered Financial Sidekick! 🤖💰

print("👋 Hey! I'm CryptoBuddy—your friendly AI financial sidekick!")
print("Ask me about crypto trends, sustainability, or long-term growth.\n")

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high", 
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

while True:
    user_query = input("You: ").lower()

    if "exit" in user_query or "bye" in user_query:
        print("CryptoBuddy: 🚀 Stay smart and stay safe! Bye!")
        break

    elif "trending" in user_query or "rising" in user_query:
        print("CryptoBuddy: Coins with a rising trend are:")
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising":
                print(f" - {coin}")

    elif "sustainable" in user_query:
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: {best} 🌱 is the most sustainable choice with low energy use and high viability!")

    elif "long-term" in user_query or "growth" in user_query:
        recommended = []
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                recommended.append(coin)
        if recommended:
            for coin in recommended:
                print(f"CryptoBuddy: Go with {coin} 🚀—rising trend and strong sustainability!")
        else:
            print("CryptoBuddy: Sorry, no coins currently meet both rising trend and strong sustainability criteria.")

    elif "help" in user_query:
        print("CryptoBuddy: Try asking:\n - Which crypto is trending?\n - What's the most sustainable coin?\n - Best for long-term growth?\nType 'exit' to quit.")

    else:
        print("CryptoBuddy: 🤖 Hmm, I’m still learning! Try asking about trends, sustainability, or long-term growth.")

print("\n⚠️ Disclaimer: Crypto is risky—always do your own research!")
