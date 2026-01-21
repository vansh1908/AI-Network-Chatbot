from chatbot import process_query

def main():
    print("🌐 Net Minds CLI (type 'exit' to quit)")
    while True:
        query = input("\nAsk: ")
        if query.lower() == "exit":
            break
        try:
            result = process_query(query)
            print(result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()