from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json.get('data')

    if not data:
        return render_template('no_results.html', message="No data provided. Please enter some transactions.")

    transactions = [item.split(',') for item in data]
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)

    if frequent_itemsets.empty:
        return render_template('no_results.html', message="No frequent itemsets found. Try lowering the minimum support threshold.")

    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

    rules_list = []
    for index, row in rules.iterrows():
        formal_rule = f"{' , '.join(list(row['antecedents']))} -> {' , '.join(list(row['consequents']))}"
        human_readable_rule = (
            f"If a customer buys {', '.join(list(row['antecedents']))}, they are "
            f"{row['confidence'] * 100:.2f}% likely to also buy {', '.join(list(row['consequents']))}. "
            f"This combination is {row['lift']:.2f} times more likely than if the items were bought independently. "
            f"The support for this rule is {row['support'] * 100:.2f}%, meaning it appears in {row['support'] * 100:.2f}% of all transactions."
        )

        rules_list.append({
            'formal_rule': formal_rule,
            'rule': human_readable_rule,
            'support': f"{row['support'] * 100:.2f}%",
            'confidence': f"{row['confidence'] * 100:.2f}%",
            'lift': f"{row['lift']:.2f}"
        })

    global rules_data
    rules_data = rules_list

    return redirect(url_for('results'))

@app.route('/results', methods=['GET'])
def results():
    if not rules_data:
        return render_template('no_results.html', message="No rules were found.")
    
    return render_template('results.html', rules=rules_data)

if __name__ == "__main__":
    rules_data = []
    app.run(debug=True)
