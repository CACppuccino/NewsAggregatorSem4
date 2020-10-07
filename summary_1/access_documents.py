import json
import summary

def main():
	x = json.loads(open ("../result.json").read())
	test_art = x[1]['art']
	print(test_art)
	print("-----------------------------------------")
	print(summary.body_summary(test_art))

if __name__ == "__main__":
    main()


