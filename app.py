import asyncio
import logging
import os
from flask import Flask, render_template, jsonify
import cognee
from main import customer_data

logger = logging.getLogger(__name__)

app = Flask(__name__)


async def run_analysis():
    cognee.config.set_llm_provider(os.environ["LLM_PROVIDER"])
    cognee.config.set_llm_model(os.environ["LLM_MODEL"])
    cognee.config.set_llm_api_key(os.environ["LLM_API_KEY"])
    cognee.config.set_embedding_provider(os.environ["EMBEDDING_PROVIDER"])
    cognee.config.set_embedding_model(os.environ["EMBEDDING_MODEL"])
    cognee.config.set_embedding_api_key(os.environ["EMBEDDING_API_KEY"])
    cognee.config.set_embedding_dimensions(int(os.environ["EMBEDDING_DIMENSIONS"]))

    await cognee.prune.prune_data()
    await cognee.prune.prune_system(metadata=True)

    for record in customer_data:
        await cognee.add(record)

    await cognee.cognify()

    query = "Which customers show signs of churn risk, and why? List each customer by name with their risk reason."
    results = await cognee.search(query_text=query)

    output = []
    for result in results:
        if isinstance(result, dict) and "search_result" in result:
            for item in result["search_result"]:
                output.append(str(item))
        else:
            output.append(str(result))
    return output


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        results = asyncio.run(run_analysis())
        return jsonify({"results": results})
    except Exception as e:
        logger.exception("Analysis failed")
        return jsonify({"error": "Analysis failed. Check server logs for details."}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

