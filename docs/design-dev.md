## **VitalEdge Embeddings**

### **Project Overview**
A RESTful FastAPI microservice for generating embeddings for text inputs. This service supports two backends:
1. **Local**: Uses Hugging Face models for on-premise, privacy-compliant embeddings.
2. **OpenAI**: Uses OpenAI’s `text-embedding-ada-002` API for high-quality embeddings.

The system is designed to work with LangChain microservices for tasks such as working with VectorDB through Retrieval-Augmented Generation (RAG).

---

## **System Design**

### **Architecture**

1. **Frontend**
   - Not applicable (API-only service).

2. **Backend**
   - FastAPI for API routing.
   - Service layer to abstract embedding generation logic.
   - Configuration layer to handle dynamic backend switching.

3. **Storage**
   - No persistent storage (stateless service).

4. **Deployment**
   - Dockerized for ease of deployment and scalability.
   - Optionally hosted on Kubernetes or other container orchestration platforms.

5. **Infrastructure**
   - Supports CPU and GPU-based inference.
   - Uses environment variables for API keys and backend configuration.

---

### **High-Level Workflow**

1. Request to `/embeddings/generate` with text input and optional backend choice.
2. Service validates the input and backend.
3. Calls the respective backend (Local or OpenAI).
4. Returns JSON response with embeddings.

---

## **API Specification**

### **Endpoints**

#### **1. `/embeddings/generate`**
- **Method**: `POST`
- **Description**: Generate embeddings for a list of text inputs.
- **Request Body**:
  ```json
  {
    "texts": ["text1", "text2"],
    "backend": "local"  // Optional: "local" or "openai". Defaults to the configured backend.
  }
  ```
- **Response**:
  ```json
  {
    "embeddings": [
      [0.123, 0.456, ...],  // Embedding for text1
      [0.789, 0.321, ...]   // Embedding for text2
    ]
  }
  ```
- **Error Codes**:
  - `400`: Invalid input or unsupported backend.

---

#### **2. `/admin/set_backend`**
- **Method**: `POST`
- **Description**: Dynamically switch the backend.
- **Request Body**:
  ```json
  {
    "backend": "local"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Backend switched to local"
  }
  ```
- **Error Codes**:
  - `400`: Invalid backend.

---

### **Core Backend Services**

#### **Local Embedding Service**
- Uses a Sentence-Transformer model from Hugging Face (`all-MiniLM-L6-v2`).
- Runs inference on CPU/GPU.

#### **OpenAI Embedding Service**
- Uses OpenAI's `text-embedding-ada-002` API.
- Requires an API key.

---

## **Development Roadmap**

### **Phase 1: Core Development (2-3 weeks)**

#### **1. Project Setup (Day 1-2)**
- Set up FastAPI project structure.
- Configure `Dockerfile` and `docker-compose.yml`.
- Add basic environment variable support (`.env` file).

#### **2. Local Backend (Day 3-5)**
- Integrate Hugging Face's Sentence-Transformer model.
- Add `LocalEmbeddingService`.

#### **3. OpenAI Backend (Day 6-8)**
- Integrate OpenAI embeddings API.
- Add `OpenAIEmbeddingService`.

#### **4. API Development (Day 9-12)**
- Create `/embeddings/generate` endpoint.
- Create `/admin/set_backend` endpoint.
- Add input validation and error handling.

---

### **Phase 2: Testing & Optimization (1-2 weeks)**

#### **1. Unit Testing (Day 13-15)**
- Write tests for embedding services.
- Write tests for API routes.

#### **2. Performance Optimization (Day 16-18)**
- Optimize Hugging Face models for inference (e.g., convert to ONNX).
- Add asynchronous processing for OpenAI API calls.

#### **3. Dockerization (Day 19-20)**
- Finalize `Dockerfile` and `docker-compose.yml`.
- Add support for multi-stage builds (optional).

---

### **Phase 3: Deployment & Documentation (1 week)**

#### **1. Deployment (Day 21-23)**
- Deploy to a cloud platform (e.g., AWS, GCP, Azure).
- Add monitoring and logging (e.g., Prometheus, Grafana).

#### **2. Documentation (Day 24-25)**
- Write API documentation (e.g., Swagger/OpenAPI spec).
- Create developer and deployment guides.

#### **3. Final Testing (Day 26-28)**
- Test end-to-end functionality.
- Fix any remaining issues.

---

### **Optional Features**

#### **1. Authentication**
- Add API key-based authentication for endpoints.

#### **2. Advanced Model Switching**
- Support runtime switching of Hugging Face models.

#### **3. Batch Processing**
- Optimize for large-scale batch embedding generation.

#### **4. Fine-Tuning**
- Add capability to fine-tune Hugging Face models on specific datasets.

---
