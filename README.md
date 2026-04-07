# EECS4312_W26_SpecChain

## Instructions

### Application
- **Wysa**
- Mental Wellbeing AI application that includes an AI mental health coach chatbot, meditation exercises and mood tracking.

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

   or

   
   ```bash
   git clone https://github.com/nvukosa97/SpecChain-214415525.git
   cd SpecChain-214415525
   ```

3. **Create environment file**
   ```bash
   cp .env.example .env
   ```

4. **Add your Groq API key (I can't upload my key due to Git security restrictions if needed please email me)**
   - Open `.env` and add:
     ```
     GROQ_API_KEY=your_actual_key_here
     ```
   - If you need a key: https://console.groq.com/keys

5. **Install dependencies**
   ```bash
   python -m pip install -r requirements.txt
   ```

6. **Run the pipeline**
   ```bash
   python src/run_all.py
   ```

7. **View results**
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

