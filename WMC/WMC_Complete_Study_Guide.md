# Wireless & Mobile Communication (WMC) — Complete Exam + Viva Guide

**How to use:** Modules 1–6 follow the syllabus order. Each topic = definition → key points → diagram/table → exam tip. Part B = lab experiments. Part C = formulas cheat sheet. **Every module ends with its own “Quick Viva Q&A” — each question is followed directly by its answer.**
**Answer pattern for any theory question:** Definition (2 lines) → Diagram → Explanation/steps → Table (if comparison) → Advantages/Applications → One-line conclusion.

## Table of Contents

1. [Module 1 — Basics of Wireless Communication](#module-1--basics-of-wireless-communication)
2. [Module 2 — Mobile Communication Generations](#module-2--mobile-communication-generations)
3. [Module 3 — Wireless Networking Technologies](#module-3--wireless-networking-technologies)
4. [Module 4 — Signal Propagation and Interference](#module-4--signal-propagation-and-interference)
5. [Module 5 — Mobile Network Architecture](#module-5--mobile-network-architecture)
6. [Module 6 — Future Trends](#module-6--future-trends-in-wireless-communication)
7. [Part B — Lab Experiments](#part-b--lab-experiments-quick-revision)
8. [Part C — Formula Cheat Sheet](#part-c--formula--number-cheat-sheet)

---

# MODULE 1 — BASICS OF WIRELESS COMMUNICATION

## 1.1 Wireless Transmission Principles

### Need for wireless communication

Wireless communication = transfer of information **without physical wires**, using EM waves (radio, microwave, infrared, satellite).

| Need | Example | Benefit |
|---|---|---|
| Mobility | Phones, smartwatches | Stay connected while moving |
| Remote/inaccessible areas | Mountains, villages, deserts | Cabling is costly/impossible |
| Fast installation | Wi-Fi in offices, event networks | Hours instead of weeks |
| Cost effectiveness | WLAN, mobile banking | No trenching/cabling cost |
| Emergency/disaster | Police, ambulance, fire radios | Works when wired lines are destroyed |
| Global internet | 4G/5G, satellite internet | Work/learn from anywhere |

**Real-world applications:** *Mobile* (calls, SMS, internet), *IoT* (smart home, agriculture, health monitoring), *Defense* (radar, secure military comms, surveillance), *Satellite* (GPS, weather, TV), *Healthcare* (telemedicine, wearables), *Transport* (GPS, railway comms).

### Wired vs Wireless

| Parameter | Wired | Wireless |
|---|---|---|
| Medium | Copper/coax/fiber | Free space (EM waves) |
| Mobility | None | Full |
| Installation | Slow, costly | Fast, cheaper |
| Data rate | Higher, stable (fiber) | Lower, variable |
| Reliability | Immune to weather/interference | Affected by interference, fading, obstacles |
| Security | Harder to tap | Easier to intercept (needs encryption) |
| Disaster resilience | Cables get cut | Quick restore via towers/satellite |
| Examples | Ethernet, PSTN, fiber | GSM/4G/5G, Wi-Fi, Bluetooth |

### Elements of a communication system

```
Source → Transmitter (encoder + modulator + antenna) → CHANNEL (+Noise) → Receiver (antenna + demodulator + decoder) → Destination
```

- **Source:** generates information (voice, data).
- **Transmitter:** converts info to a signal suited for the channel (coding, modulation, amplification).
- **Channel:** medium between Tx and Rx; for wireless = free space. Adds **path loss, noise, fading, interference**.
- **Receiver:** picks up weak signal, demodulates, decodes.
- **Destination:** end user/device.

### Path loss (qualitative)

Signal power reduces as distance increases because energy spreads over a larger area (**inverse-square law: Pr ∝ 1/d²**). Also depends on frequency (higher f → more loss), environment, obstacles.

- Free-space: `PL(dB) = 32.44 + 20 log10(d_km) + 20 log10(f_MHz)`
- Log-distance model: `PL(dB) = PL(d0) + 10·n·log10(d/d0)` (n = path-loss exponent: ~2 free space, 3–5 urban).
- Effect: limits range → need more base stations / higher power / better antennas.

## 1.2 Frequency Spectrum Allocation

**EM spectrum** (low → high frequency): Radio → Microwave → Infrared → Visible → Ultraviolet → X-ray → Gamma. Wireless comms uses the **radio/microwave region** (3 Hz–300 GHz): non-ionizing, long range, penetrates obstacles. Relation: **λ = c/f** (c = 3×10⁸ m/s).

| Band | Range | Use |
|---|---|---|
| VLF/LF | <300 kHz | Submarine comm, navigation |
| MF | 300 kHz–3 MHz | AM radio (520–1605 kHz) |
| HF | 3–30 MHz | Shortwave radio |
| VHF | 30–300 MHz | FM radio (87.5–108 MHz), TV |
| UHF | 300 MHz–3 GHz | Mobile (GSM 900/1800), Wi-Fi 2.4, TV |
| SHF | 3–30 GHz | Satellite (C, Ku), radar, 5G mid/mmWave, Wi-Fi 5 GHz |
| EHF | 30–300 GHz | mmWave 5G, imaging, radar |

**Trend:** higher frequency → smaller antennas, more bandwidth, but shorter range & poorer obstacle penetration. UHF is the "sweet spot" for mobile.

### Licensed vs Unlicensed

| | Licensed | Unlicensed (ISM) |
|---|---|---|
| Access | Exclusive to operator (govt auction) | Anyone following power rules |
| Cost | Very high | Free |
| Interference | Protected | Not protected |
| Examples | 2G/3G/4G/5G, TV/radio, satellite | Wi-Fi, Bluetooth, Zigbee (2.4 GHz, 5 GHz, 868/915 MHz) |

**Why regulate spectrum?** Finite resource → avoid interference, ensure global interoperability (ITU; in India DoT/WPC/TRAI).

## 1.3 Introduction to Cellular Communication

**Cellular concept:** divide a large area into small **cells**, each with a low-power **base station**. Same frequencies are **reused** in distant cells → huge capacity with limited spectrum.

- **Why hexagon?** Tiles a plane with no gaps/overlap and is closest to the circular coverage of an antenna (fewest cells to cover an area). Real cells are irregular.
- **Cluster (N):** group of N cells using all available channels once. `N = i² + ij + j²` → valid N = 1, 3, 4, 7, 9, 12, 13…
- **Co-channel cells:** cells using the same frequency group.

### Formulas

| Quantity | Formula |
|---|---|
| Total channels | S = k·N (k = channels per cell) |
| Frequency reuse factor | 1/N |
| Reuse distance | D = R√(3N) |
| Co-channel reuse ratio | Q = D/R = √(3N) |
| Capacity with M clusters | C = M·k·N = M·S |
| Signal-to-interference | S/I = Qⁿ / i₀ (n≈4, i₀ = 6) |

**Trade-off:** small N → more channels per cell (high capacity) but co-channel cells close → more interference. Large N → less interference, less capacity. **N = 7** is the classic compromise (S/I ≈ 18.7 dB, needed ≈ 18 dB for voice).

**Numerical example:** R = 2 km, N = 7 → D = 2√21 = **9.16 km**; reuse factor = 1/7 ≈ 0.143.

**Capacity-improvement methods:** cell splitting, sectoring (120° sectors), microcells/small cells.
**Cell sizes:** Macro (km) > Micro (city block) > Pico (building) > Femto (home).
**Handover** = call moves to next cell while user moves (see Module 5).


### ✅ Quick Viva Q&A — Module 1

**Q1. Wireless communication?**  
**A:** Info transfer without wires using EM waves.

**Q2. Why hexagonal cells?**  
**A:** No gaps/overlap; nearest to circular coverage.

**Q3. Frequency reuse?**  
**A:** Same frequencies reused in far-apart cells to increase capacity.

**Q4. Cluster?**  
**A:** N cells using all channels once.

**Q5. Valid N values?**  
**A:** 1, 3, 4, 7, 9, 12 (from i²+ij+j²).

**Q6. Why N = 7?**  
**A:** Balance of interference (S/I ≈ 18.7 dB ≥ 18 dB) and capacity.

**Q7. Licensed vs unlicensed?**  
**A:** Licensed = paid exclusive (cellular); unlicensed = free shared ISM (Wi-Fi, Bluetooth).

**Q8. Which band for mobile?**  
**A:** UHF (and SHF for 5G).

**Q9. Higher frequency →?**  
**A:** Smaller antenna, more bandwidth, shorter range.

**Q10. Ways to increase capacity?**  
**A:** Cell splitting, sectoring, smaller cells, lower N.

---

# MODULE 2 — MOBILE COMMUNICATION GENERATIONS

## 2.1 Limitations of wired communication → need for mobility

Fixed location; costly/slow cabling; hard in remote areas; cables vulnerable in disasters; not scalable (new user = new line); no mobility for users. → Led to cellular mobile systems.

## 2.2 Evolution 1G → 5G

| Gen | Year | Tech/Standard | Switching | Speed | Service |
|---|---|---|---|---|---|
| 1G | 1980s | AMPS (analog, FDMA) | Circuit | ~2.4 kbps | Analog voice only |
| 2G | 1990s | GSM (TDMA/FDMA), IS-95 (CDMA), digital | Circuit | 9.6–14.4 kbps | Digital voice, SMS, encryption |
| 2.5G | 2000 | GPRS | Circuit + packet | ~115–171 kbps | MMS, always-on internet |
| 2.75G | | EDGE | | ~384 kbps | Faster data |
| 3G | 2000s | UMTS/WCDMA, HSPA | Hybrid | 2 Mbps (HSPA+ up to 42) | Mobile internet, video call |
| 4G | 2010s | LTE / LTE-A (OFDMA, MIMO) | All-IP packet | 100 Mbps–1 Gbps | HD streaming, VoLTE, cloud |
| 5G | 2020s | 5G NR (massive MIMO, slicing) | All-IP, cloud core | 10–20 Gbps | IoT, AR/VR, autonomous, remote surgery |

| Feature | 3G | 4G | 5G |
|---|---|---|---|
| Base station | NodeB + RNC | eNodeB | gNB |
| Core | CS + PS (MSC, SGSN, GGSN) | EPC (all-IP) | 5GC (service-based, cloud) |
| Access | WCDMA | OFDMA (DL), SC-FDMA (UL) | OFDMA + massive MIMO |
| Latency | 100–500 ms | ~20–50 ms | ~1 ms |
| Voice | Circuit switched | VoLTE | VoNR |
| Key limitation solved | Data on mobile | Broadband speed, all-IP | Latency, device density, IoT |

**Limitation of each generation:** 1G – analog, no security, poor capacity; 2G – low data rate; 3G – latency/bandwidth insufficient for data explosion; 4G – cannot support IoT density/ultra-low latency.
**Compare any 2 generations:** pick two columns from the table above + advantages/disadvantages/applications.

## 2.3 GSM Architecture (simplified)

```
 MS ──Um──> BTS ──Abis──> BSC ──A──> MSC ──> PSTN / GMSC
 (ME+SIM)     \_____ BSS _____/       |
                               HLR  VLR  AuC  EIR   OMC (OSS)
                               \____ NSS ____/
```

GSM = 2G digital cellular. Three subsystems:

**1. BSS (Base Station Subsystem / Radio subsystem)**

- **MS:** Mobile Equipment (handset) + **SIM** (stores IMSI, Ki). Connects via Um (air) interface.
- **BTS:** transceiver + antenna of a cell; handles radio link with MS; one per cell/sector.
- **BSC:** controls many BTSs; radio resource management, handover (within BSC), power control, maps Um channels to A interface.

**2. NSS (Network & Switching Subsystem)**

- **MSC:** heart of network — call setup, routing, release, mobility management, handover (between BSCs), billing data.
- **GMSC:** gateway MSC to PSTN/other networks; queries HLR for incoming calls.
- **HLR:** permanent database — subscriber profile, services, current location (VLR/MSC address).
- **VLR:** temporary database of subscribers currently in an MSC's area (copied from HLR).
- **AuC:** stores secret key Ki; generates authentication triplets (RAND, SRES, Kc).
- **EIR:** database of IMEIs — white (valid), grey (monitor), black (stolen/blocked).

**3. OSS:** **OMC** — operation & maintenance, fault monitoring, performance, network management.

**Interfaces:** Um (MS–BTS), Abis (BTS–BSC, 16 kbps channels), A (BSC–MSC, 64 kbps).
**GSM air interface facts:** 900 MHz band: UL 890–915 MHz, DL 935–960 MHz; 25 MHz each; 200 kHz carrier spacing → 124 carriers; **8 time slots/carrier (TDMA)**; GMSK modulation; 270.833 kbps per carrier; frame = 4.615 ms, slot = 577 µs; duplex spacing 45 MHz. Also GSM 1800 (1710–1785 / 1805–1880 MHz).

## 2.4 CDMA concept (spread spectrum)

**Multiple access methods:** FDMA (split by frequency), TDMA (split by time), **CDMA (split by code — all users share the same time and frequency, each with a unique code)**.

**Spread spectrum:** deliberately spread signal over a bandwidth much wider than required, using a code independent of data. Benefits: resistance to narrowband interference/jamming, anti-fading, low probability of interception, multiple access (CDMA). Cost: complex, needs synchronization & power control.

### DSSS (Direct Sequence)

- Each data bit **XOR** with a fast **chipping sequence** (e.g., 11-chip **Barker code `10110111000`**) → bandwidth ×11. **Processing gain = chip rate / bit rate = 11 (≈10.4 dB)**.
- **Tx:** User data ⊕ chipping sequence → spread signal → modulator (× radio carrier) → transmit.
- **Rx:** Demodulator (× carrier) → **correlator** (XOR with same code + integrator) → decision → data.
- **Example:** data `01`. Bit 0 → code unchanged `10110111000`; bit 1 → inverted `01001000111`. Rx XOR with same code → 0 gives all 0s (sum 0), 1 gives all 1s (sum 11). Decision rule: sum < 4 → 0, sum > 7 → 1.
- **Noise tolerance:** even if 1–2 chips flip, sums become e.g. 2 and 10 → still decoded as 0 and 1.
- **Barker code:** sharp autocorrelation (matches itself only when aligned) → easy sync. Used in 802.11b.
- **Uses:** CDMA, 802.11b Wi-Fi, GPS, cordless phones.
- Pros: anti-jamming, anti-interception, anti-fading. Cons: precise power control, complex, sync needed.

### FHSS (Frequency Hopping)

- Bandwidth split into many channels; Tx & Rx **hop** between them in a pre-agreed **hopping sequence**; time on one channel = **dwell time**. (FDM + TDM combination.)
- **Slow hopping:** several bits per hop. Cheaper, relaxed sync, less immune. Used in **GSM**.
- **Fast hopping:** several hops per bit. Better interference resistance, more secure, complex, tight sync. Used in **Bluetooth** (1600 hops/s, 79 channels × 1 MHz).
- **Tx:** data → modulator → narrowband signal → 2nd modulator with carrier f_i from **frequency synthesizer** (driven by hopping sequence) → spread signal.
- **Rx:** demodulator using synchronized synthesizer → narrowband → demodulator → data.

| FHSS | DSSS |
|---|---|
| Multiple frequencies used | Single frequency |
| Hard to find user's frequency | Frequency stays same |
| Frequency reuse allowed | Not allowed |
| Cheaper | More expensive |

### CDMA key points

Each user has a unique (orthogonal) code; Rx despreads only its own code; others look like noise. Features: **soft handover**, universal frequency reuse (N=1), power control essential (**near-far problem**), "soft capacity". Used in IS-95 (2G), WCDMA (3G).

## 2.5 LTE / 4G basics

- **Goals:** high data rate (100 Mbps–1 Gbps), low latency, **all-IP packet switching** (no circuit switching; voice = VoLTE), flat architecture, scalable bandwidth 1.4–20 MHz.
- **Radio tech:** **OFDMA** downlink (wide channel → many orthogonal narrow subcarriers in parallel; resists multipath/ISI), **SC-FDMA** uplink (lower peak-to-average power → battery saving), **MIMO** (multiple antennas → higher rate), 64-QAM modulation.
- **Architecture:** UE → **E-UTRAN (eNodeB)** → **EPC**.

| Element | Function |
|---|---|
| eNodeB | Base station; radio + RNC functions merged; X2 link between eNodeBs |
| MME | Control plane: authentication, mobility, paging, bearer setup (no user data) |
| S-GW | User-plane anchor during handover; forwards packets |
| P-GW | Gateway to Internet (PDN); IP allocation |
| HSS | Subscriber database/keys (≈HLR+AuC) |
| PCRF | Policy & charging rules (QoS, billing) |

**Flow (YouTube):** UE → eNodeB → MME (checks HSS) → S-GW → P-GW → Internet. Control (MME) and data (S/P-GW) are separate.

## 2.6 Introduction to 5G

5G = ultra-fast, ultra-low-latency, massively connected network for people, machines, things. Peak 10–20 Gbps, ~1 ms latency, ~10⁶ devices/km².

**Three use-case categories (ITU IMT-2020):**

| | eMBB | URLLC | mMTC |
|---|---|---|---|
| Full form | Enhanced Mobile Broadband | Ultra-Reliable Low-Latency Comm | Massive Machine-Type Comm |
| Focus | Speed & capacity | ~1 ms latency, 99.999% reliability | Device density, low power |
| Examples | 4K/8K, AR/VR, cloud gaming | Remote surgery, autonomous cars, factory control | Smart meters, soil sensors, smart city |

**Key technologies:** NR air interface, **massive MIMO**, **beamforming**, **network slicing**, mmWave + sub-6 GHz, virtualization/cloud-native core, edge computing.


### ✅ Quick Viva Q&A — Module 2

**Q11. 1G vs 2G?**  
**A:** Analog vs digital (voice + SMS).

**Q12. 2.5G?**  
**A:** GPRS packet data.

**Q13. 3G tech?**  
**A:** UMTS/WCDMA.

**Q14. 4G tech?**  
**A:** LTE, all-IP, OFDMA/SC-FDMA/MIMO.

**Q15. Why SC-FDMA in uplink?**  
**A:** Low PAPR → saves phone battery.

**Q16. VoLTE?**  
**A:** Voice as data over LTE.

**Q17. GSM access method?**  
**A:** TDMA/FDMA, 8 slots per 200 kHz carrier.

**Q18. Role of BTS/BSC/MSC?**  
**A:** Radio / controls BTSs & handover / switching & call routing.

**Q19. HLR vs VLR?**  
**A:** Permanent home database vs temporary visitor database.

**Q20. AuC / EIR?**  
**A:** Keys & authentication / IMEI blacklist.

**Q21. Interfaces?**  
**A:** Um, Abis, A.

**Q22. CDMA?**  
**A:** All users share band using unique codes.

**Q23. DSSS vs FHSS?**  
**A:** Spread by code vs hop frequencies.

**Q24. Chip?**  
**A:** One bit of spreading code.

**Q25. Where is FHSS used?**  
**A:** Bluetooth (fast hopping), GSM (slow hopping option).

**Q26. Near-far problem?**  
**A:** Strong near user swamps weak far user; fixed by power control.

**Q27. eNodeB vs NodeB?**  
**A:** eNodeB has RNC functions merged (flat).

**Q28. MME/S-GW/P-GW/HSS/PCRF?**  
**A:** Control & mobility / user-plane anchor / Internet gateway & IP / subscriber DB / policy & billing.

**Q29. eMBB, URLLC, mMTC?**  
**A:** Speed / low latency & reliability / massive IoT.

**Q30. Network slicing?**  
**A:** Multiple virtual networks on same physical infrastructure.

**Q31. gNB?**  
**A:** 5G base station.

---

# MODULE 3 — WIRELESS NETWORKING TECHNOLOGIES

## 3.1 Wi-Fi (IEEE 802.11)

- WLAN technology for high-speed internet. **Infrastructure mode:** devices connect via **Access Point (AP)** in **star topology**; **ad hoc mode:** device-to-device.
- **Working:** AP broadcasts **beacon frames** (contain **SSID**) → device scans, selects network → authentication (WPA2/WPA3) → association → **DHCP** gives IP → all traffic through AP/router → Internet.
- **Access method:** **CSMA/CA** (listen before transmit, avoid collisions; wireless can't detect collisions).
- Bands: 2.4, 5, 6 GHz. 2.4 GHz: longer range, slower, crowded (non-overlapping channels 1, 6, 11). 5 GHz: faster, shorter range.

| Standard | Name | Band | Max rate |
|---|---|---|---|
| 802.11b | – | 2.4 | 11 Mbps (DSSS) |
| 802.11a | – | 5 | 54 Mbps |
| 802.11g | – | 2.4 | 54 Mbps |
| 802.11n | Wi-Fi 4 | 2.4/5 | 600 Mbps |
| 802.11ac | Wi-Fi 5 | 5 | ~3.5 Gbps |
| 802.11ax | Wi-Fi 6/6E | 2.4/5/6 | ~9.6 Gbps |
| 802.11be | Wi-Fi 7 | 2.4/5/6 | 30+ Gbps |

- **Security:** WEP (weak) < WPA < **WPA2 (AES)** < WPA3.
- Range ≈ 50 m indoor, 100 m outdoor.
- Applications: home/office internet, hotspots, streaming, CCTV, smart TV.
- Pros: high data rate, widely supported. Cons: high power, interference, limited range.

## 3.2 Bluetooth (IEEE 802.15.1)

- Short-range (≈10 m Class 2; 100 m Class 1; 1 m Class 3) WPAN, 2.4 GHz ISM, **FHSS** (79 channels, 1 MHz spacing, 1600 hops/s) for interference resistance. Data rate 1–3 Mbps (BLE 1–2 Mbps).
- **Piconet:** 1 **master** + up to **7 active slaves** (255 parked). **Scatternet:** several piconets linked by a device that belongs to more than one.
- **Working:** device discovery (inquiry) → **pairing** (PIN/passkey, shared link key) → connection → data in **time slots (TDD)**, master controls timing & hop sequence.
- **BLE** (Bluetooth 4.0+): very low power for wearables/sensors.
- Applications: earbuds, speakers, keyboard/mouse, smartwatch, car hands-free, file transfer.
- Pros: low cost, low power, no line-of-sight. Cons: short range, low rate, max 7 active slaves.

## 3.3 Zigbee (IEEE 802.15.4)

- Low-power, low-rate WPAN for IoT/sensor/control networks. 2.4 GHz (also 868/915 MHz). **250 kbps**, range 10–100 m per hop, **65,000+ nodes**, battery life years.
- **Device roles:** **Coordinator** (one; starts & manages network), **Router** (relays messages; mains powered), **End device** (battery sensor; sleeps most of the time).
- **Topologies:** star, tree, **mesh** (self-healing, multi-hop → extends range & reliability).
- Applications: smart home (bulbs, locks), smart meters, industrial/building automation, agriculture, healthcare monitoring.
- Pros: ultra low power, mesh, scalable, cheap. Cons: very low data rate, not for streaming.

## 3.4 NFC — Near Field Communication

- Contactless communication by **magnetic induction** between two loop antennas; **13.56 MHz**; range **≤ 4 cm**; data rate **106/212/424 kbps**; standards ISO 14443 / ISO 18092 / NFC Forum.
- **Modes:** (1) **Reader/Writer** (phone reads a tag), (2) **Peer-to-peer** (phone to phone share), (3) **Card emulation** (phone acts as card — payments, tickets).
- **Devices:** *Active* (has own power, generates field — phone) vs *Passive* (tag, powered by reader's field, no battery).
- Security comes from **very short range** + encryption for payments.
- Applications: contactless payment (Google Pay/Apple Pay), metro/transit cards, door access, ID/passport, quick pairing for Bluetooth/Wi-Fi, smart posters.
- Pros: instant setup, secure, low power. Cons: very short range, low data rate.

## 3.5 Comparison of technologies

| | Wi-Fi | Bluetooth | Zigbee | NFC |
|---|---|---|---|---|
| Standard | 802.11 | 802.15.1 | 802.15.4 | ISO 14443/18092 |
| Network type | WLAN | WPAN | WPAN (LR-WPAN) | Proximity |
| Frequency | 2.4/5/6 GHz | 2.4 GHz | 2.4 GHz (868/915) | 13.56 MHz |
| Range | ~50 m (indoor) | ~10 m | 10–100 m (mesh more) | ≤ 4 cm |
| Data rate | up to Gbps | 1–3 Mbps | 250 kbps | 106–424 kbps |
| Power | High | Low (BLE very low) | Very low | Very low/passive |
| Topology | Star | Piconet/scatternet | Mesh/star/tree | Point-to-point |
| Max devices | ~250/AP | 8 per piconet | 65,000+ | 2 |
| Use | Internet, streaming | Audio, peripherals | IoT, sensors | Payments, access |

**Which to choose?** Speed → Wi-Fi; personal gadget nearby → Bluetooth; many battery sensors → Zigbee; tap-and-go → NFC.

## 3.6 Wireless Sensor Networks (WSN)

- **WSN** = many small, low-cost, battery-powered **sensor nodes** spread over an area that sense (temp, humidity, motion, gas), process locally and send data wirelessly (often multi-hop) to a **sink/base station → gateway → internet/cloud**.
- **Node components:** sensor(s), microcontroller, transceiver (radio), power source (battery/solar), memory.
- **Topologies:** star, tree, mesh/multi-hop. Technologies: Zigbee, BLE, LoRa, 6LoWPAN.
- **Characteristics:** self-organizing, energy constrained, large scale, fault tolerant.
- **Challenges:** limited battery (energy-efficient routing, sleep modes), limited memory/compute, security, scalability, reliability.
- **Applications:** environment monitoring, military surveillance, health, agriculture, smart city, industrial.

## 3.7 Use cases

- **Smart home:** PIR (motion), DHT11 (temp/humidity), MQ-2 (gas) sensors → ESP32 (Wi-Fi) → cloud (MQTT/Blynk/Firebase) → app; relay switches appliances; Zigbee/BLE for battery devices; alerts on gas/fire.
- **Healthcare:** wearable pulse/SpO₂/ECG sensors → BLE → phone → cloud → doctor alerts; telemedicine, remote patient monitoring.
- **Agriculture:** soil-moisture/temperature sensors → Zigbee/LoRa → gateway → automatic irrigation pump; crop monitoring, drones.


### ✅ Quick Viva Q&A — Module 3

**Q32. Wi-Fi standard & access method?**  
**A:** 802.11; CSMA/CA.

**Q33. SSID? Beacon?**  
**A:** Network name; frame AP broadcasts with SSID.

**Q34. DHCP?**  
**A:** Auto-assigns IP, mask, gateway.

**Q35. WPA2 encryption?**  
**A:** AES.

**Q36. Piconet?**  
**A:** 1 master + up to 7 active slaves.

**Q37. Scatternet?**  
**A:** Interconnected piconets.

**Q38. Why Bluetooth hops?**  
**A:** Avoid interference, add security.

**Q39. Zigbee roles?**  
**A:** Coordinator, router, end device.

**Q40. Why Zigbee for sensors?**  
**A:** Very low power, mesh, many nodes.

**Q41. NFC range/frequency?**  
**A:** ≤4 cm, 13.56 MHz.

**Q42. NFC modes?**  
**A:** Reader/writer, peer-to-peer, card emulation.

**Q43. Passive NFC tag?**  
**A:** Powered by reader's field.

**Q44. WSN?**  
**A:** Many sensor nodes sending data to a sink wirelessly.

**Q45. WSN main challenge?**  
**A:** Limited energy.

**Q46. WPAN vs WLAN?**  
**A:** Personal (metres) vs local (building).

---

# MODULE 4 — SIGNAL PROPAGATION AND INTERFERENCE

## 4.1 Basics of wave propagation

- **LOS (Line-of-Sight):** direct unobstructed path; strongest, most reliable (microwave links, satellite).
- **NLOS (Non-LOS):** direct path blocked; signal reaches via reflection, diffraction, scattering (typical in cities/indoors) → weaker, multipath.
- **Propagation modes:** ground wave (low freq, follows earth), sky wave (HF, ionosphere reflection), space/LOS wave (VHF and above).

### Three propagation mechanisms

| | Reflection | Diffraction | Scattering |
|---|---|---|---|
| Meaning | Wave **bounces** off surface | Wave **bends** around edges | Wave **spreads** in many directions |
| Obstacle size | ≫ λ, smooth | Large with sharp edge | ≤ or ≈ λ, small/irregular |
| Objects | Buildings, ground, water, mountains | Building corners, hill ridges | Trees, lamp posts, vehicles, rough surfaces |
| Result | Extra path (weaker) | Signal in shadow region (weaker) | Many weak paths |

Other effects: **refraction** (bending when medium density changes), **absorption**, **blocking**.

## 4.2 Path loss and shadowing (conceptual)

| | Path Loss | Shadowing |
|---|---|---|
| Cause | Spreading of energy with distance | Large obstacles (buildings, hills) |
| Depends on | Distance, frequency | Environment/location |
| Nature | Gradual, predictable | Random, sudden, localized |
| Effect | Limits range | Dead zones |
| Example | Walking away from router | Entering basement/behind building |
| Fix | More BTS, taller/high-gain antennas | Small cells, repeaters, better placement |

Shadowing = *large-scale/slow fading*. Real signal = path loss + shadowing + multipath fading (graph: straight declining line + slow wiggles + fast ripples).

## 4.3 Multipath fading (real-life effect: call drops)

- **Multipath:** receiver gets several copies of signal via direct + reflected + diffracted + scattered paths with different **amplitude, phase, delay**.
- **Constructive** (in phase → stronger) vs **destructive** (out of phase → cancel → **deep fade**). Movement of a few cm changes phases → rapid fluctuation.
- **Delay spread:** difference in arrival times → **Inter-Symbol Interference (ISI)**. **Doppler spread:** frequency shift due to motion.
- **Fast fading:** rapid changes over short distance/time (moving vehicle). **Slow fading:** gradual (walking behind building).
- **Effects:** signal fluctuation, higher BER, ISI, phase distortion, **call drops** (signal falls below threshold and handover fails; other causes: path loss, shadowing, congestion).
- **Mitigation:** diversity (space/time/frequency), equalization, OFDM, RAKE receiver (CDMA), adaptive modulation, error-correcting codes, MIMO.

## 4.4 Noise types

**Noise** = unwanted random signal that degrades quality → lowers SNR → higher BER.

| Type | Cause |
|---|---|
| **Thermal (Johnson–Nyquist)** | Random electron motion in components; always present; white noise |
| Shot | Discrete charge carriers in semiconductors |
| Flicker (1/f) | Device imperfections, low frequencies |
| Burst | Semiconductor defects |
| **External:** Atmospheric | Lightning, thunderstorms |
| Man-made | Motors, ignition, power lines, switching (impulse noise) |
| Extraterrestrial/cosmic | Sun, stars, galaxies |
| **Interference** | Other radio signals (co-channel, adjacent channel) |

- **Thermal noise power: N = k·T·B** (k = 1.38×10⁻²³ J/K, T in K, B in Hz). At 290 K: **N₀ ≈ −174 dBm/Hz**; N(dBm) = −174 + 10 log₁₀(B).
- **SNR = Signal power / Noise power** ; SNR(dB) = 10 log₁₀(S/N). High SNR → clear, low BER; low SNR → errors, drops.
- **Thermal vs External:** thermal – internal, always present, ∝ T·B, controlled by cooling/LNA/narrow bandwidth; external – outside, varies with place/time, controlled by shielding/filtering/site choice.
- **Interference measures:** SIR = S/I, SINR = S/(I+N).

## 4.5 Sources of interference

**Co-Channel Interference (CCI):** from cells using the **same frequency** (due to frequency reuse). Causes: reuse, small reuse distance/cluster, high transmit power, propagation. Effect: lower SIR, BER↑, call drops, lower capacity. Depends on **Q = D/R = √(3N)** (not on power).

**Adjacent Channel Interference (ACI):** leakage from **nearby frequency** channels. Causes: imperfect filters, spectral leakage, non-linearities, strong nearby transmitter (**near-far effect**), insufficient channel spacing. Effect: distortion, errors. Example: overlapping Wi-Fi channels.

| | CCI | ACI |
|---|---|---|
| Frequency | Same | Nearby |
| Cause | Frequency reuse | Imperfect filtering |
| Depends on | Reuse distance | Frequency separation |
| Reduced by | Larger N/D, sectoring, power control | Better filters, guard bands |

## 4.6 Simple mitigation techniques

1. **Power control:** transmit minimum power needed (near tower → low, far → high) → less interference, longer battery life.
2. **Frequency planning:** reuse with sufficient distance (↑N), good channel allocation (no adjacent channels in neighbouring cells), **guard bands**, dynamic allocation.
3. **Sectoring / directional antennas:** fewer co-channel interferers (6 → 2 for 120° sectors).
4. **Better filters** (ACI), **channel separation**, **interference cancellation**, inter-cell coordination.

| Technique | Targets |
|---|---|
| Power control | CCI & ACI |
| Larger reuse distance | CCI |
| Sectoring | CCI |
| Filters/guard bands | ACI |
| Dynamic allocation | Both |


### ✅ Quick Viva Q&A — Module 4

**Q47. LOS vs NLOS?**  
**A:** Direct path vs via reflection/diffraction/scattering.

**Q48. Reflection / diffraction / scattering?**  
**A:** Bounce / bend / spread.

**Q49. Path loss vs shadowing?**  
**A:** Distance-based gradual vs obstacle-based random.

**Q50. Multipath?**  
**A:** Multiple copies of signal via different paths.

**Q51. Why call drops?**  
**A:** Destructive interference/deep fade, shadowing, failed handover.

**Q52. Fast vs slow fading?**  
**A:** Rapid (movement/Doppler) vs gradual (obstacles).

**Q53. Delay spread →?**  
**A:** ISI.

**Q54. Thermal noise formula?**  
**A:** N = kTB.

**Q55. SNR?**  
**A:** Signal power / noise power.

**Q56. CCI vs ACI?**  
**A:** Same vs adjacent frequency.

**Q57. Reuse ratio?**  
**A:** Q = D/R = √(3N).

**Q58. Mitigation?**  
**A:** Power control, frequency planning, sectoring, filters, guard bands.

**Q59. Guard band?**  
**A:** Unused gap between channels.

**Q60. Near-far effect in ACI?**  
**A:** Strong adjacent transmitter overwhelms weak desired signal.

---

# MODULE 5 — MOBILE NETWORK ARCHITECTURE

## 5.1 Cellular network components

```
UE ──radio──> RAN (BTS/NodeB/eNodeB/gNB) ──> Core Network ──> Internet / PSTN
```

- **User Equipment (UE):** phone/IoT device (ME + SIM/USIM).
- **BTS / RAN:** radio access — towers + controller (BSC/RNC); 4G: eNodeB; 5G: gNB.
- **Core Network:** authentication, mobility, switching, billing, gateway to external networks. 2G/3G: MSC, VLR, HLR, GMSC (+SGSN/GGSN for data). 4G: EPC (MME, SGW, PGW, HSS). 5G: AMF, SMF, UPF, UDM.

## 5.2 Call flow (simplified call setup)

**Signalling** (control) first → then **voice**.

### Mobile-Originated (MO) call (A calls someone)

Steps: User dials → **call request** (MS → BSS → MSC) → **identification & authentication** (MSC ↔ VLR) → **destination determination** → **resource preparation** (traffic channel, free circuit) → **call establishment** (via GMSC/PSTN) → called party answers → **speech**.
Numbered (GSM): 1–2 connection request; 3–4 security check (MSC–VLR); 5–8 check resources (BSS assigns TCH, MSC checks circuit); 9–10 set up call (MSC → GMSC → PSTN).

### Mobile-Terminated (MT) call (someone calls the mobile)

Main problem: **locate the mobile**.

1. Caller dials MSISDN; 2. PSTN → **GMSC**; 3. GMSC asks **HLR** (signals call setup); 4. HLR requests **MSRN** from current **VLR**; 5. VLR returns MSRN; 6. HLR → GMSC (routing info); 7. GMSC forwards call to **visited MSC**; 8–9. MSC gets MS status from VLR; 10–11. MSC orders **paging** in all cells of the **location area**; 12–14. MS responds; 15. VLR security check (authentication); 16–17. MSC sets up connection → phone rings → speech.
**Paging:** network knows only the location area, so broadcasts a paging message in all its cells to find the idle mobile.

| | MO | MT |
|---|---|---|
| Started by | Mobile user | Anyone (any network) |
| Location lookup | Not needed | HLR → VLR → MSRN |
| Paging | No | Yes |
| Main challenge | Set up outgoing connection | Locate called mobile |

**Call release:** either side ends → release signalling → connection terminated → resources freed.

## 5.3 Handover concept

**Handover (handoff):** transferring an **ongoing call/data session** from one cell to another as user moves, without interruption. (*Cell reselection* = same for idle mode.)

**Why required:** user moves out of range; weaker signal/quality; better neighbouring cell; interference; **load balancing**; avoids call drops.
**Process:** Measurement → Decision → Target-cell selection → Execution → Transfer of connection → Release of old resources.
**Decision:** MS reports signal levels; handover when `neighbour level > serving level + HO_MARGIN` (hysteresis prevents **ping-pong** effect).

**Types (by entities):**

1. **Intra-cell** — same BTS, channel/timeslot changes (due to interference).
2. **Inter-cell (intra-BSC)** — BTS changes, same BSC.
3. **Inter-BSC (intra-MSC)** — BSC changes, same MSC.
4. **Inter-MSC** — MSC changes.

**Types (by behaviour):**

| | Hard (break-before-make) | Soft (make-before-break) |
|---|---|---|
| Old link | Released before new set up | Kept until new link ready |
| Interruption | Short possible | None |
| Resources | Lower | Higher |
| Used in | GSM, LTE | CDMA/3G WCDMA |

(*Softer* handover = between sectors of same BTS.) Also *MCHO/NCHO/MAHO*: MS/network/mobile-assisted — GSM uses **MAHO**.

**GSM procedure (inter-BSC):** MS measurement report → BSC_old decision → "HO required" to MSC → MSC "HO request" to BSC_new → resource allocation/channel activation at BTS_new → ack → "HO command" to MS → MS "HO access" on new BTS → link established → "HO complete" → MSC "clear command" → old resources released.

## 5.4 Roaming

**Roaming** = using voice/SMS/data on a **visited network** outside your **home network**, with same number/SIM, enabled by **inter-operator agreements**.

- **National roaming:** another operator, same country. **International roaming:** operator in another country.
- **Home network:** keeps permanent record (HLR, AuC), authenticates, bills subscriber. **Visited network:** gives radio service, temp record in **VLR**, records usage, settles with home operator.
- **Procedure:** phone attaches to visited network → VLR identifies subscriber (IMSI/TMSI; MCC+MNC give home network) → **location update** to HLR (HLR stores new VLR/MSC; sends profile to VLR; cancels old VLR) → authentication triplets from AuC → services provided → incoming calls routed GMSC → HLR → VLR (MSRN) → usage records (TAP) exchanged → home operator bills.
- **Roaming vs Handover:** roaming = service through another network; handover = moving an active call between cells.
- **Challenges:** cost, billing complexity, frequency band/technology compatibility, security, QoS variation.

## 5.5 Role of SIM, IMSI, authentication (basic security)

**SIM:** smart card storing **IMSI**, secret key **Ki**, A3/A8 algorithms, PIN, TMSI, LAI.

**Identifiers:**

| ID | Meaning |
|---|---|
| **IMSI** | MCC (3) + MNC (2–3) + MSIN; unique subscriber identity (internal), India MCC 404/405 |
| **MSISDN** | Phone number = CC + NDC + SN |
| **TMSI** | 4-byte temporary ID assigned by VLR → hides IMSI over the air |
| **IMEI** | 15-digit handset ID (used by EIR) |
| **MSRN** | Temporary roaming number from VLR, used to route incoming calls |

**Authentication (A3) & key generation (A8) & encryption (A5):**

| Algo | Job | Inputs | Output | Where |
|---|---|---|---|---|
| A3 | Authentication | Ki (128) + RAND (128) | SRES (32 bit) | SIM + AuC |
| A8 | Cipher key generation | Ki + RAND | Kc (64 bit) | SIM + AuC |
| A5 | Encryption of air link | Kc + frame no. | keystream (XOR with data) | Phone + BTS |

**Memory trick:** 3 = check, 8 = key, 5 = lock.
**Procedure:** MS sends TMSI/IMSI → network gets **triplet (RAND, XRES, Kc)** from AuC → sends only **RAND** to MS → SIM computes SRES = A3(Ki,RAND) and Kc = A8(Ki,RAND) → MS sends SRES → network compares SRES == XRES → match = allowed → traffic encrypted by A5 using Kc.
**Why secure:** **Ki never travels**; RAND/SRES change every time.
**A5 versions:** A5/0 none; **A5/1** strong (3 LFSRs 19+22+23 = 64 bits, majority clocking); A5/2 weak (banned); A5/3 KASUMI (3G cipher).
**Weaknesses:** one-way auth (network doesn't authenticate to phone → fake base stations/IMSI catchers); COMP128, A5/1 cracked; only air interface encrypted; short 64-bit key. **3G fixed with mutual authentication (AKA).**

## 5.6 Introduction to packet core networks (data services)

**Why packet switching:** internet traffic is bursty; circuit switching wastes resources (GSM CSD only 9.6 kbps). Packet switching shares resources, charges by data volume.

**GPRS (2.5G)** — packet data over GSM: 1–8 timeslots per user, 9–171 kbps, always-on, volume-based billing, voice & data simultaneously.

- **Changes to GSM:** **PCU** (Packet Control Unit) added to BSC (voice → MSC, data → SGSN); HLR gets GPRS subscriber data; MSC/VLR stores SGSN number.
- **SGSN (Serving GPRS Support Node)** ≈ "MSC for packet domain": packet delivery to/from MS, **authentication, registration (attach), mobility management**, charging info collection.
- **GGSN (Gateway GPRS Support Node):** gateway to external **PDN (Internet/X.25)**; routing info, **address conversion**/IP allocation, stores current SGSN address & user profile, tunnelling.
- **IP backbone with GTP** (GPRS Tunnelling Protocol) between SGSN and GGSN.
- **Interfaces:** Um (MS–BSS), Gb (BSS–SGSN), Gn (SGSN–GGSN), Gi (GGSN–PDN), Gr (to HLR).

```
MS ─Um─ BTS ─ BSC+PCU ─Gb─ SGSN ─Gn(GTP/IP backbone)─ GGSN ─Gi─ Internet
                 └─voice─> MSC               HLR/VLR/EIR
```

- **Handset classes:** A (voice+data simultaneously), B (either, auto switch), C (manual switch).

| GSM | GPRS |
|---|---|
| Circuit switched | Packet switched |
| 1 slot/user | Multiple slots/user |
| Billing by time | Billing by data |
| 9.6 kbps | up to ~171 kbps |

**Evolution:** 3G packet core = SGSN/GGSN (UMTS); **4G EPC:** SGSN → MME + S-GW, GGSN → P-GW; **5G core:** AMF, SMF, UPF.


### ✅ Quick Viva Q&A — Module 5

**Q61. MO vs MT?**  
**A:** Outgoing vs incoming; MT needs HLR/VLR lookup & paging.

**Q62. MSRN?**  
**A:** Temporary routing number from VLR.

**Q63. Paging?**  
**A:** Broadcast to find idle mobile in location area.

**Q64. Handover vs roaming?**  
**A:** Active call cell change vs use of another operator's network.

**Q65. Hard vs soft handover?**  
**A:** Break-before-make (GSM/LTE) vs make-before-break (CDMA).

**Q66. HO_MARGIN?**  
**A:** Hysteresis threshold; avoids ping-pong.

**Q67. Four GSM handovers?**  
**A:** Intra-cell, inter-cell, inter-BSC, inter-MSC.

**Q68. Roaming types?**  
**A:** National, international.

**Q69. IMSI/MSISDN/TMSI/IMEI?**  
**A:** Subscriber ID / phone number / temporary ID / handset ID.

**Q70. Why TMSI?**  
**A:** Hides IMSI over air.

**Q71. A3/A8/A5?**  
**A:** Authentication / key generation / encryption.

**Q72. Is Ki sent over air?**  
**A:** Never.

**Q73. Weakness of GSM security?**  
**A:** One-way authentication (fake towers).

**Q74. GPRS?**  
**A:** Packet-switched data over GSM (2.5G).

**Q75. SGSN vs GGSN?**  
**A:** Serves mobiles (auth, mobility) vs gateway to Internet (IP, routing).

**Q76. PCU?**  
**A:** Packet Control Unit in BSC separating data to SGSN.

**Q77. GTP?**  
**A:** Tunnelling protocol between SGSN and GGSN.

**Q78. EPC equivalent of SGSN/GGSN?**  
**A:** MME+S-GW / P-GW.

---

# MODULE 6 — FUTURE TRENDS IN WIRELESS COMMUNICATION

## 6.1 5G architecture (high level)

```
UE ──5G NR radio──> gNB ──N2 (control)──> AMF ── SMF ── UPF ──N6──> Internet/Cloud
                       └──────────N3 (user data)────────> UPF
```

- **UE:** phone, vehicle, IoT. **gNB:** 5G base station (radio, resource mgmt, massive MIMO, beamforming). **5GC:** software-based, **service-based architecture (SBA)**, cloud-native. **Data network:** Internet/cloud/edge.

| NF | Function | 4G equivalent |
|---|---|---|
| AMF | Registration, mobility, access authentication | MME (part) |
| SMF | Session management, IP allocation | MME (session) + parts of SGW/PGW |
| UPF | User-plane forwarding, traffic/charging | S-GW + P-GW |
| AUSF | Authentication server | HSS (part) |
| UDM | Unified Data Management (subscriber data) | HSS |
| PCF | Policy control & QoS | PCRF |
| NRF | Network function registration/discovery | — (like DNS) |
| SEPP | Secure inter-operator (roaming) signalling (N32) | — |

**Key enabling technologies:** **Massive MIMO** (many antennas, many users), **Beamforming** (focus energy on user), **Network slicing** (virtual networks on shared infra: eMBB/URLLC/mMTC slices), **Infrastructure virtualization/decoupling** (NFV/SDN), **Edge computing**, mmWave, small cells.
**Deployment:** NSA (non-standalone, uses 4G core) vs SA (standalone, 5GC). Bands: low (<1 GHz, coverage), mid (3.5 GHz n78, balance), high mmWave (24–100 GHz, speed).

## 6.2 Applications of 5G

- **Smart cities:** traffic management, smart parking, street lights, surveillance, waste, grid, public safety.
- **Autonomous/connected vehicles:** V2V, V2I, V2P (V2X), drones, platooning (URLLC).
- **Healthcare:** remote surgery, telemedicine, patient monitoring, medical imaging.
- **Industry 4.0:** smart factory, robots, predictive maintenance.
- **Consumer:** 4K/8K video, cloud gaming, AR/VR, fixed wireless access (FWA).
- **Others:** smart agriculture, energy/smart grid, logistics, remote education.

| 5G capability | Benefit |
|---|---|
| Low latency | Autonomous vehicles, surgery |
| High data rate | Real-time video/AR |
| Massive connectivity | Millions of IoT sensors |
| Slicing | Dedicated resources per service |
| Edge computing | Faster local decisions |

## 6.3 IoT ecosystem

**IoT** = network of physical objects with sensors, connectivity and software that collect/exchange/act on data. (IoT thermometer vs ordinary: sends data to cloud.)

**Components:** (1) Devices/sensors & actuators, (2) Connectivity network, (3) Gateway/connectivity management platform, (4) Cloud/edge processing, (5) AI & analytics, (6) Applications (dashboard/apps).

- **Sensor** measures (temperature, motion, gas); **Actuator** acts (motor, relay, valve, buzzer).

**Four-layer architecture:** 1 Things/Sensing → 2 Connectivity/Network → 3 Processing/Platform (edge/cloud) → 4 Application.

**Working:** Sense → Collect → Communicate → Process → Decide → Act. *Example (smart irrigation):* soil sensor → gateway → LoRaWAN/4G → cloud → moisture low → command → pump ON.

| Technology | Range | Rate | Use |
|---|---|---|---|
| BLE | Short | Low | Wearables |
| Wi-Fi | Short | High | Cameras, appliances |
| Zigbee | Short (mesh) | Low | Smart home |
| LoRaWAN | Long (km) | Very low | Agriculture, meters |
| NB-IoT | Wide (cellular) | Low | Smart meters, tracking |
| 4G/5G | Wide | High | Industrial, vehicles |

**Protocols:** MQTT (publish/subscribe, lightweight), CoAP, HTTP. **Benefits:** monitoring, automation, efficiency. **Challenges:** security/privacy, interoperability, power, scale, data management.

## 6.4 Smart devices and connected systems

- **Smart devices:** objects with sensing + processing + connectivity: smartphones, smartwatches, smart speakers (Alexa), smart bulbs/plugs/locks, thermostats, connected cars, wearables, industrial sensors.
- **Connected systems:** smart home, smart city, connected vehicle (V2X), connected healthcare, Industrial IoT, smart grid.
- **Features:** remote monitoring/control, automation, data-driven decisions, interoperability. **Concerns:** security (use WPA2/3, TLS), privacy, dependence on internet/power, cost, compatibility.
- **Relay:** 3.3 V board switches 230 V appliance.

## 6.5 Edge computing and AI in telecom (introductory)

**Edge computing / MEC (Multi-access Edge Computing):** processing near the user (at base station/local data centre) instead of distant cloud → **low latency, less backhaul traffic, better privacy, real-time response** (autonomous vehicles, AR/VR, industrial control, video analytics).

**AI/ML in telecom:**

- **Self-Organizing Networks (SON):** auto-configure, optimise, heal.
- **Predictive maintenance:** detect faults before failure.
- **Traffic prediction & resource allocation**, load balancing, network slicing management.
- **Energy saving:** switch off idle cells.
- **Anomaly/fraud detection**, security, customer churn prediction, chatbots.
- **Smart beamforming**, interference management, channel estimation.
- **Edge AI:** AI inference at edge for real-time decisions.

## 6.6 Future directions: 6G vision (conceptual)

- Expected ~**2030**. Targets: **~1 Tbps peak** (50–100× 5G), **~0.1 ms latency**, extreme reliability, massive connectivity (10⁷ devices/km²).
- **Technologies:** **terahertz (sub-THz, 0.1–10 THz)** spectrum, **AI-native networks**, **integrated sensing and communication** (network as radar), **reconfigurable intelligent surfaces (RIS)**, cell-free massive MIMO, **non-terrestrial networks** (satellites/HAPS/drones – global coverage), quantum-safe security, energy efficiency/green networks.
- **Applications:** holographic communication, digital twins, extended reality (XR), tactile internet, fully autonomous systems, brain-computer interfaces.
- **Challenges:** THz propagation loss & short range, hardware cost, energy, security/privacy, standardisation.

| 5G | 6G (vision) |
|---|---|
| ~20 Gbps | ~1 Tbps |
| ~1 ms | ~0.1 ms |
| mmWave | THz |
| AI-assisted | AI-native |
| Terrestrial focus | Space-air-ground integration |


### ✅ Quick Viva Q&A — Module 6

**Q79. 5G core functions?**  
**A:** AMF, SMF, UPF, UDM, AUSF, PCF, NRF.

**Q80. Massive MIMO / beamforming?**  
**A:** Many antennas / focused beams.

**Q81. Four IoT layers?**  
**A:** Things, connectivity, processing, application.

**Q82. Sensor vs actuator?**  
**A:** Measures vs acts.

**Q83. MQTT?**  
**A:** Lightweight publish/subscribe IoT protocol.

**Q84. LoRaWAN vs NB-IoT?**  
**A:** Unlicensed long-range low-rate vs cellular licensed IoT.

**Q85. Edge computing benefit?**  
**A:** Low latency, less backhaul.

**Q86. AI in telecom?**  
**A:** SON, predictive maintenance, traffic prediction, energy saving.

**Q87. 6G target?**  
**A:** ~1 Tbps, ~0.1 ms, THz, AI-native, sensing + communication.

**Q88. RIS?**  
**A:** Reconfigurable intelligent surface to steer signals.

---

# PART B — LAB EXPERIMENTS (Quick Revision)

| # | Experiment | Core idea / tool | Key result & viva points |
|---|---|---|---|
| 1 | **Frequency reuse** (Python/matplotlib) | Input N, R → hex grid labelled A–G; red dashed line shows D | D = R√3N; N=7,R=1 → D=4.58. Small N = capacity↑ interference↑ |
| 2 | **DSSS with Barker code** (Python) | Each bit XOR 11-chip Barker `10110111000`; Rx XOR again | Input 1011 → recovered 1011. Chip = code bit; processing gain 11; XOR twice = original |
| 3 | **GSM security A3/A5/A8** (Python, SHA-256 stand-in) | SRES = A3(Ki,RAND), Kc = A8(Ki,RAND), A5 stream cipher | Genuine passes, impostor with wrong Ki fails; Ki never sent |
| 4 | **Wireshark** | Capture on Wi-Fi; filters tcp, udp, dns, arp, ssdp | See below |
| 5 | **iPerf3** | `iperf3 -s` (server/receiver), `iperf3 -c <IP>` (client/sender), port 5201, 10 s | Throughput ≈ 9.4 Mbits/s on 10 Mbps link (< bandwidth due to header overhead). Latency via `ping` |
| 6 | **Wi-Fi in Cisco Packet Tracer** | WRT300N router, SSID "Home Router", WPA2-PSK/AES, DHCP from 192.168.0.2 (50 users), laptops with WPC300N card | Ping 0% loss; TTL 255 router, 128 Windows PC |
| 7 | **ESP32 Wi-Fi scan + BLE scan** (Arduino IDE) | `WiFi.scanNetworks()` in WIFI_STA mode → SSID, RSSI, channel; BLE scan → name, MAC, RSSI; baud 115200 | RSSI closer to 0 = stronger (−40 excellent, −90 unusable) |
| 8 | **Cellular parameters on smartphone** | Android `*#*#4636#*#*` / iPhone `*3001#12345#*` / Cell Info apps; note RSRP, RSRQ, SINR at window/room/lift | Strongest near window, weakest in lift |
| 9 | **Wi-Fi vs Bluetooth vs Zigbee** | Comparison (see 3.5) | – |
| 10 | **Smart home** | Sensors + ESP32 + relay + cloud (MQTT) + app | IoT = sensors + connectivity + cloud + app |

### Wireshark details

- Capture filter (BPF, before capture) vs Display filter (after). Panes: Packet List, Packet Details (layer tree), Packet Bytes (hex/ASCII). Colours: light purple TCP, light blue UDP, cream ARP, pink ICMP, green HTTP, dark grey SYN/FIN, dark maroon RST, black bad TCP.
- **Encapsulation:** Frame → Ethernet II (MAC, EtherType 0x0800 IPv4 / 0x0806 ARP) → IPv4 (protocol 6=TCP, 17=UDP, 1=ICMP) → TCP/UDP (ports) → data. **ARP has no IP layer.**
- **TCP:** reliable, connection-oriented; 3-way handshake **SYN → SYN-ACK → ACK**; FIN closes; RST aborts; header min 20 B; filter `tcp.flags.syn==1`; HTTPS port 443 (TLS encrypted).
- **UDP:** connectionless, no ACK, fast; header **8 bytes** (src port, dst port, length, checksum); used for DNS, QUIC, video, games.
- **DNS:** UDP port 53; query and response share the **Transaction ID**; A = IPv4, AAAA = IPv6, CNAME = alias; example claude.ai → 160.79.104.10.
- **ARP:** request = **broadcast** (ff:ff:ff:ff:ff:ff), opcode 1, target MAC 00:..; reply = **unicast**, opcode 2. IP → MAC.
- **SSDP:** UPnP discovery, multicast 239.255.255.250, UDP 1900, M-SEARCH/NOTIFY.
- Promiscuous mode = NIC accepts all frames; driver Npcap; file saved as .pcapng; Windows TTL 128, Linux 64.
- Filter cheat sheet: `ip.addr==x`, `tcp.port==443`, `dns || arp`, `!arp`, `tcp && ip.addr==x`.

### Cellular parameter ranges (4G)

| | Excellent | Good | Fair | Poor |
|---|---|---|---|---|
| RSRP (dBm) | > −80 | −80 to −90 | −90 to −100 | < −100 |
| RSRQ (dB) | > −10 | −10 to −15 | −15 to −20 | < −20 |
| SINR (dB) | > 20 | 13–20 | 0–13 | < 0 |

RSRP = tower reference signal power (main strength); RSSI = total received power; RSRQ = RSRP vs RSSI (quality); SINR = signal vs interference+noise (decides speed); 3G equivalents RSCP & Ec/Io; ASU: dBm = ASU − 140. Other IDs: Cell ID, PCI, MCC/MNC (India 404/405), band/EARFCN, TAC/LAC.


### ✅ Quick Viva Q&A — Lab Experiments

**Q89. Capture vs display filter?**  
**A:** Before vs after capture.

**Q90. TCP handshake?**  
**A:** SYN, SYN-ACK, ACK.

**Q91. UDP header size?**  
**A:** 8 bytes.

**Q92. ARP request vs reply?**  
**A:** Broadcast vs unicast; opcode 1/2.

**Q93. iPerf3 server/client flags?**  
**A:** `-s` / `-c IP`; port 5201.

**Q94. Bandwidth vs throughput?**  
**A:** Capacity vs achieved rate.

**Q95. RSSI meaning?**  
**A:** Received signal strength in dBm; closer to 0 stronger.

**Q96. RSRP/RSRQ/SINR?**  
**A:** Strength / quality / signal vs interference+noise.

**Q97. WIFI_STA vs WIFI_AP?**  
**A:** Client mode vs hotspot mode.

**Q98. Why relay in smart home?**  
**A:** Low-voltage MCU controls high-voltage appliance.

**Q99. Barker code used in?**  
**A:** 802.11b DSSS.

**Q100. Processing gain?**  
**A:** Chip rate / bit rate.

---

# PART C — FORMULA & NUMBER CHEAT SHEET

| Item | Value/Formula |
|---|---|
| λ | c/f, c = 3×10⁸ m/s |
| Cluster size | N = i² + ij + j² (1,3,4,7,9,12…) |
| Channels | S = kN ; reuse factor 1/N |
| Reuse distance | D = R√(3N); Q = D/R = √(3N) |
| S/I | Qⁿ / i₀ ; n≈4, i₀=6 ; N=7 → ≈18.7 dB |
| Thermal noise | N = kTB ; k = 1.38×10⁻²³ ; −174 dBm/Hz at 290 K |
| SNR | S/N ; dB = 10 log₁₀(S/N) |
| Path loss | Pr ∝ 1/d² ; PL = PL(d0) + 10 n log(d/d0) |
| Processing gain (DSSS) | chip rate / bit rate = 11 (10.4 dB) |
| GSM | UL 890–915, DL 935–960 MHz; 200 kHz; 8 slots; GMSK; 270.8 kbps; 124 carriers |
| Bluetooth | 79 ch, 1 MHz, 1600 hops/s, 7 active slaves |
| Zigbee | 250 kbps, 65,000 nodes |
| NFC | 13.56 MHz, ≤4 cm, 106–424 kbps |
| 5G | 20 Gbps, 1 ms, 10⁶ devices/km² |
| Key sizes | Ki 128, RAND 128, SRES 32, Kc 64 bits |

---

# Notes on source corrections

- **SNR = Signal/Noise** (some slides write it inverted).
- **Reuse ratio Q = D/R** (some slides write R/D).
- **UDM = Unified Data Management** (a slide says "Repository").
- Latency figures vary by source (4G ~20–50 ms); quote "~20–50 ms" if unsure.
- Details for NFC, Wi-Fi standards, WSN, edge/AI and 6G come from standard reference material (no slides were provided for them) — cross-check with your class notes.
