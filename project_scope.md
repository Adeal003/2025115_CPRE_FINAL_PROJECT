# Musical Instrument Classification FPGA Project Checklist
## Team 14: Chilana Amaratunga, Bibidh Bista, Ashley Deal, Shivansh Patel

---

## Week 1: Dataset Preparation & Initial Model Training

### Dataset Selection & Setup
- [ Done - IRMAS ] Choose between NSynth or IRMAS dataset
- [ DONE ] Download and organize dataset on HPC cluster
- [ DONE ] Verify dataset integrity and structure
- [ DONE ] Document dataset characteristics (number of classes, samples per class, audio format)

### Audio Preprocessing Pipeline
- [DONE ] Install required Python libraries (librosa, TensorFlow, NumPy, etc.)
- [DONE ] Set up Python virtual environment (`python3 -m venv project_venv`)
- [DONE ] Implement audio loading functions
- [ DONE] Implement spectrogram generation pipeline
- [ DONE] Create visualization functions for spectrograms
- [ DONE ] Test preprocessing on sample audio files
- [ DONE ] Document preprocessing parameters (FFT size, hop length, etc.)

### Initial Model Development
- [ DONE] Adapt CNN architecture for audio spectrograms
- [ DONE] Define model layers (Conv2D, ReLU, MaxPooling, Dense, Softmax)
- [DONE ] Implement data augmentation (if applicable)
- [DONE  ] Set up training/validation/test split
- [ DONE ] Create Jupyter notebook for training pipeline

### Checkpoint: Dataset ready, preprocessing working, model architecture defined

---

## Week 2: Model Training & Profiling

### Model Training
- [DONE ] Train initial model on GPU VM (cpre587-f25-*.ece.iastate.edu)
- [ DONE] Experiment with different batch sizes
- [DONE ] Monitor training progress (loss, accuracy curves)
- [DONE ] Validate model performance on test set
- [ DONE] Document final hyperparameters
- [ DONE] Save trained model weights

### Model Profiling with TensorBoard
- [DONE ] Set up TensorBoard profiling
- [DONE ] Profile single inference latency
- [DONE ] Profile batch inference throughput
- [ DONE] Analyze layer-wise computation time
- [DONE ] Identify performance bottlenecks
- [DONE ] Export profiling results and visualizations
- [DONE ] Document findings in notebook

### Model Export
- [DONE ] Export trained weights as binary files
- [ DONE] Export biases as binary files
- [ DONE] Generate test vectors (input audio → intermediate features → output)
- [ DONE] Save intermediate feature maps for validation
- [DONE ] Verify exported data integrity

### Checkpoint: Trained model achieving target accuracy, profiling complete

---

## Week 3: Software Quantization & C++ Implementation

### Quantization Framework
- [ ] Implement Float32 → Int8 quantization scripts
- [ ] Calculate scale factors and zero-points per layer
- [ ] Quantize all weights and biases
- [ ] Validate quantized model accuracy vs. float32 baseline
- [ ] Document accuracy degradation (should be minimal)
- [ ] Export quantized weights/biases for C++ and hardware

### C++ Layer Implementations
- [ ] Set up C++ development environment
- [ ] Implement Convolution layer (2D conv with 8-bit arithmetic)
- [ ] Implement ReLU activation
- [ ] Implement MaxPooling layer
- [ ] Implement Flatten layer
- [ ] Implement Fully-connected (Dense) layer
- [ ] Implement Softmax layer
- [ ] Create test cases for each layer

### C++ Integration & Validation
- [ ] Integrate all layers into complete inference pipeline
- [ ] Load quantized weights/biases into C++ program
- [ ] Run inference on test audio samples
- [ ] Validate C++ outputs against Python quantized model
- [ ] Fix any discrepancies
- [ ] Profile C++ inference using `perf` tool
- [ ] Document CPU inference performance (latency, throughput)

### Checkpoint: C++ quantized inference working and validated

---

## Week 4: FPGA Hardware Design

### MAC Unit Design - Staged Version
- [ ] Review Lab 3 MAC unit design
- [ ] Modify for 8-bit fixed-point arithmetic
- [ ] Implement AXI-Stream interface
- [ ] Create VHDL testbench for staged MAC
- [ ] Verify functional correctness in simulation
- [ ] Document MAC unit specifications

### MAC Unit Design - Pipelined Version (Optional)
- [ ] Design pipelined MAC architecture
- [ ] Implement pipelined version in VHDL
- [ ] Create testbench for pipelined MAC
- [ ] Verify timing and throughput improvements
- [ ] Compare staged vs. pipelined performance

### Vivado Project Setup
- [ ] Open Vivado template project (`cd <path to lab>/simple_interface/vivado/`)
- [ ] Run `source simple_interface.tcl` to generate project
- [ ] Open block design
- [ ] Verify Zynq PS + PL configuration
- [ ] Add staged MAC unit to block design
- [ ] Configure AXI-Stream FIFO connections
- [ ] Set `C_DATA_WIDTH` to 8 for int8 MAC

### Synthesis & Implementation
- [ ] Run synthesis in Vivado
- [ ] Review synthesis warnings/errors
- [ ] Analyze resource utilization (LUTs, FFs, DSPs, BRAMs)
- [ ] Run implementation
- [ ] Analyze timing reports (check for timing violations)
- [ ] Optimize if needed to meet timing
- [ ] Document achieved clock frequency

### Bitstream Generation
- [ ] Generate bitstream (.bit file)
- [ ] Export hardware specification (.xsa file)
- [ ] Save synthesis reports for final report
- [ ] Document FPGA resource usage

### Checkpoint: FPGA design synthesized, bitstream ready

---

## Week 5: ZedBoard Integration & Testing

### Vitis Firmware Development
- [ ] Open Vitis IDE (Path: `/remote/Xilinx/2020.1/Vitis/2020.1/bin/vitis`)
- [ ] Create new Vitis project for ZedBoard
- [ ] Import hardware specification (.xsa)
- [ ] Set up C++ firmware project

### Hardware-Software Interface
- [ ] Modify Conv layer to use `computeAccelerated()` function
- [ ] Modify Dense layer to use `computeAccelerated()` function
- [ ] Implement AXI-Stream FIFO register access
- [ ] Implement data packing (8-bit pairs → 16-bit packets)
- [ ] Implement data unpacking (16-bit → 8-bit results)
- [ ] Send test data to FPGA MAC units via FIFO
- [ ] Read results from FPGA MAC units

### ZedBoard Testing
- [ ] Build firmware in Vitis
- [ ] Program ZedBoard with bitstream
- [ ] Load firmware onto ARM processor
- [ ] Run simple MAC unit tests
- [ ] Verify hardware MAC results match software MAC
- [ ] Debug any discrepancies

### Full Inference on ZedBoard
- [ ] Port complete inference pipeline to ZedBoard
- [ ] Load quantized weights/biases onto board
- [ ] Run inference on test audio samples
- [ ] Validate ZedBoard outputs match C++ software results
- [ ] Measure inference latency on ZedBoard
- [ ] Document performance metrics

### Performance Evaluation
- [ ] Create evaluation scripts for automated testing
- [ ] Measure inference latency (single sample)
- [ ] Measure throughput (samples/second)
- [ ] Compare accuracy: FPGA vs. software quantized vs. float32
- [ ] Collect resource utilization data from Vivado
- [ ] Measure power consumption (if feasible)
- [ ] Generate comparison tables and plots

### Checkpoint: Full system working on ZedBoard, performance data collected

---

## Week 6: Final Report & Demo Preparation

### Final Report Writing
- [ ] **Executive Summary/Abstract** - Concise overview of project
- [ ] **Introduction & Motivation** - Problem statement, real-world applications
- [ ] **Background & Related Work** - Literature review (5-10 peer-reviewed papers for 5870)
- [ ] **Methodology**
  - [ ] Dataset description (NSynth/IRMAS)
  - [ ] Audio preprocessing pipeline
  - [ ] CNN architecture details
  - [ ] Quantization strategy (Float32 → Int8)
  - [ ] FPGA hardware design (MAC units, Zynq integration)
- [ ] **Experimental Setup**
  - [ ] Training configuration (batch size, epochs, optimizer, etc.)
  - [ ] Hardware platforms (GPU VM specs, ZedBoard specs)
  - [ ] Evaluation metrics definitions
- [ ] **Results & Analysis**
  - [ ] Accuracy comparison (Float32 vs. Int8)
  - [ ] Performance metrics tables (latency, throughput)
  - [ ] FPGA resource utilization charts
  - [ ] Power/energy measurements (if available)
  - [ ] Comparative analysis: FPGA vs. CPU vs. GPU
- [ ] **Discussion** - Interpretation, limitations, challenges
- [ ] **Conclusion & Future Work**
- [ ] **References** - Properly formatted citations
- [ ] **Appendices** - Additional plots, data tables, code snippets

### Code Documentation
- [ ] Clean up all Python code
- [ ] Add comprehensive comments to C++ code
- [ ] Add comments to VHDL/Verilog files
- [ ] Create README files for each component
- [ ] Document build/run instructions
- [ ] Ensure reproducibility

### Demo Preparation
- [ ] Create presentation slides (8-10 slides)
- [ ] Write demo script
- [ ] Select 3-5 audio samples for live demonstration
- [ ] Test ZedBoard setup multiple times
- [ ] Practice presentation (10-15 minutes target)
- [ ] Prepare backup plan (video recording if hardware fails)
- [ ] Record demo video as backup

### Final Assembly
- [ ] Export Jupyter notebook to PDF
- [ ] Generate final report PDF (`project_report_14.pdf`)
- [ ] Organize all deliverables by category
- [ ] Create compressed archive (.tgz or .zip)
- [ ] Verify all files are included and accessible
- [ ] Test archive extraction on different machine

### Submission
- [ ] Double-check deliverables against requirements
- [ ] Submit to Canvas before deadline
- [ ] Confirm submission received
- [ ] Prepare for demo presentation

### Checkpoint: Everything submitted, ready for final presentation

---

## Deliverables Checklist

### 1. Written Report
- [ ] PDF format: `project_report_14.pdf`
- [ ] 15-25 pages
- [ ] All required sections complete
- [ ] Figures and tables properly labeled
- [ ] References properly formatted

### 2. Jupyter Notebook
- [ ] `.ipynb` file: `project_notebook_14.ipynb`
- [ ] PDF export: `project_notebook_14.pdf`
- [ ] All cells executed with outputs
- [ ] Code documented with comments
- [ ] Visualizations included

### 3. Software Quantization Framework
- [ ] Quantization scripts (Python)
- [ ] Validation scripts
- [ ] Binary weight/bias exports

### 4. C++ Inference Implementation
- [ ] All layer implementations
- [ ] Main inference pipeline code
- [ ] Profiling scripts
- [ ] Build instructions (Makefile/README)

### 5. FPGA Hardware Design
- [ ] VHDL/Verilog source files (staged MAC)
- [ ] VHDL/Verilog source files (pipelined MAC - optional)
- [ ] Testbenches
- [ ] Vivado project files
- [ ] Bitstream (.bit file)
- [ ] Hardware spec (.xsa file)
- [ ] Synthesis reports

### 6. ZedBoard Integration
- [ ] Vitis project files
- [ ] Modified C++ layer implementations with hardware acceleration
- [ ] FIFO interface code
- [ ] Build instructions

### 7. Evaluation Suite
- [ ] Performance measurement scripts
- [ ] Results data (CSV/JSON)
- [ ] Comparison plots
- [ ] Analysis scripts

### 8. Demo Presentation
- [ ] Presentation slides
- [ ] Demo script
- [ ] Sample audio files
- [ ] Backup video (if applicable)

---

## Risk Mitigation Strategies

### If Behind Schedule in Weeks 1-2 (Model Training)
- [ ] Use smaller dataset subset (3-5 instruments instead of 10)
- [ ] Reduce training epochs (prioritize "good enough" accuracy)
- [ ] Use existing librosa functions without custom implementations

### If Behind Schedule in Weeks 3-4 (FPGA Design)
- [ ] Reuse Lab 3 MAC unit with minimal modifications
- [ ] Skip pipelined MAC variant (focus on staged only)
- [ ] Use provided Vivado templates without custom optimizations

### If Behind Schedule in Week 5 (Integration)
- [ ] Accelerate only Conv layers (skip Dense layer acceleration)
- [ ] Use pre-validated test vectors instead of live audio
- [ ] Simplify demo to offline results presentation

### If Behind Schedule in Week 6 (Documentation)
- [ ] Focus on core sections (skip extensive appendices)
- [ ] Use existing plots without creating new visualizations
- [ ] Simplify demo to presentation + video backup

---

## Notes & Resources

### Important Paths
- **Vivado**: `/remote/Xilinx/2020.1/Vivado/2020.1/bin/vivado`
- **Vitis**: `/remote/Xilinx/2020.1/Vitis/2020.1/bin/vitis`
- **Lab Template**: `<path to lab>/simple_interface/vivado/`

### Key Resources
- GPU VM: `cpre587-f25-*.ece.iastate.edu`
- ZedBoard documentation
- Lab 3 materials (MAC unit reference)
- TensorFlow quantization guides
- librosa documentation

### Team Communication
- [ ] Set up regular team meetings (weekly minimum)
- [ ] Assign component ownership per team member
- [ ] Create shared repository for code/documents
- [ ] Establish communication channel (Slack, Discord, etc.)

---

## Progress Tracking

**Current Phase**: _______________

**Completion Status**: _____ / _____ tasks complete

**Next Milestone**: _______________

**Blockers/Issues**: 
- 
- 
- 

**Notes**: