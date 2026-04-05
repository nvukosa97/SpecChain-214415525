# EECS4312_W26_SpecChain

## Instructions

### Application
- **Wysa**

### Dataset
- Data collected using Google Play scraper  
- Original dataset: `data/reviews_raw.jsonl`  
- Cleaned dataset: `data/reviews_clean.jsonl`  
- Total cleaned reviews: **46227**

### Setup & Run Pipeline

1. **Clone the repository**
   ```bash
   git clone git@github.com:nvukosa97/SpecChain-214415525.git
   cd SpecChain-214415525
   ```

2. **Create environment file**
   ```bash
   cp .env.example .env
   ```

3. **Add your Groq API key**
   - Open `.env` and add:
     ```
     GROQ_API_KEY=your_actual_key_here
     ```
   - If you need a key: https://console.groq.com/keys

4. **Install dependencies**
   ```bash
   python -m pip install -r requirements.txt
   ```

5. **Run the pipeline**
   ```bash
   python src/run_all.py
   ```

6. **View results**
   - Open: `metrics/metrics_summary.json`  
   - Note: Comparison metrics may differ from original metrics

---

## Repository Structure

```
data/        # Datasets and review groups
personas/    # Persona files
spec/        # Specifications
tests/       # Validation tests
metrics/     # Metric outputs
src/         # Executable Python scripts
reflection/  # Final reflection
```

---

## Dataset Files

- `reviews_raw.jsonl` → Collected raw reviews  
- `reviews_clean.jsonl` → Cleaned dataset  

