import_elements_query = ["""
MERGE (e:Element {name: "Pt"})
MERGE (e1:Element {name: "C"})
MERGE (m:Physical:Enginereed:EngineeredMaterial:CarbonSupport {})
"""]
import_fabians_data_query = ["""
LOAD CSV WITH HEADERS FROM 'file:///simulation1.csv' AS line
CREATE (mol:Virtual:Matter:Molecule{uid: randomUUID(), nAtoms: line.nAtoms, weight: line.MolecularWeightgmol})
CREATE (me:Virtual:Process:Measurement {uid: randomUUID()})
CREATE(mol)-[r:measured] -> (me)
MERGE (pr:Physical:PhysicalDimension:Property {type: "SinglePointEnergy"})
CREATE(me)-[r1:yieldsQuant {value: line.SinglePointEnergyau}] -> (pr)

MERGE (pr2:Physical:PhysicalDimension:Property {type: "DipoleMoment"})
CREATE(me)-[r2:yieldsQuant {value: line.DipoleMomentDebye}] -> (pr2)

MERGE (pr3:Physical:PhysicalDimension:Property {type: "HOMO-1"})
CREATE(me)-[r3:yieldsQuant {value: line.HOMOIkJmol}] -> (pr3)

MERGE (pr4:Physical:PhysicalDimension:Property {type: "HOMO"})
CREATE(me)-[r4:yieldsQuant {value: line.HOMOkJmol}] -> (pr4)

MERGE (pr5:Physical:PhysicalDimension:Property {type: "LUMO"})
CREATE(me)-[r5:yieldsQuant {value: line.LUMOkJmol}] -> (pr5)

MERGE (pr6:Physical:PhysicalDimension:Property {type: "LUMO+1"})
CREATE(me)-[r6:yieldsQuant {value: line.LUMOIkJmol}] -> (pr6)

"""]
import_data_query = ["""
LOAD CSV WITH HEADERS FROM 'file:///InsituMeas.csv' AS line
CREATE (d:Physical:Enginereed:EngineeredDevice:FuelCell {uid: randomUUID()})
MERGE (m1:Physical:Enginereed:EngineeredMaterial:Catalyst {name: line.Catalyst})
MERGE (m2:Physical:Enginereed:EngineeredMaterial:CoatingSubstrate {name: line.Coating_substrate})
MERGE (m3:Physical:Enginereed:EngineeredMaterial:TransferSubstrate {name: line.Transfer_substrate})
MERGE (m4:Physical:Enginereed:EngineeredMaterial:Ionomer {name: line.Ionomer})
MERGE (c:Physical:Enginereed:EngineeredComponent:Membrane {name: line.Membrane})
MERGE (c1:Physical:Enginereed:EngineeredComponent:Anode {name: line.Anode})
MERGE (c2:Physical:Enginereed:EngineeredComponent:GDL {name: line.GDL})
MERGE (c3:Physical:Enginereed:EngineeredComponent:Station {name: line.Station})
CREATE (p:Physical:Process:Manufacturing {uid: randomUUID()})
CREATE (m5:Physical:Enginereed:EngineeredMaterial:Catalyst {name: "CatalystPowder", type: "CatalystInkPrecursor"})
CREATE(m1)-[r:processed] -> (p)
CREATE(m:Physical:Enginereed:EngineeredMaterial:CarbonSupport {})-[r1:processed] -> (p)
CREATE(p)-[r2:fabricates] -> (m5)
CREATE (m6:Physical:Enginereed:EngineeredMaterial:Catalyst {uid: randomUUID(), type: "CatalystInkPrecursor"})
CREATE (p1:Physical:Process:Manufacturing {uid: randomUUID()})
MERGE (pa:Physical:Process:Parameter {type: "MillingTime"})
CREATE(m5)-[r3:processed] -> (p1)-[r4:usesParameter {value: line.Drymill_time_hrs }]->(pa)
CREATE(p1)-[r5:fabricates] -> (m6)
CREATE (p2:Physical:Process:Manufacturing {uid: randomUUID()})
CREATE(m6)-[r6:processed] -> (p2)
CREATE(m4)-[r7:processed] -> (p2)
CREATE(m7:Physical:Enginereed:EngineeredMaterial:CatalystInk {uid: randomUUID()})
CREATE(p2)-[r8:fabricates] -> (m7)
MERGE(m8:Physical:Enginereed:EngineeredMaterial:CoatingSubstrate {name: line.Coating_substrate})
MERGE(m9:Physical:Enginereed:EngineeredMaterial:TransferSubstrate {name: line.Transfer_substrate})
CREATE (p3:Physical:Process:Manufacturing {uid: randomUUID()})
CREATE(m8)-[r9:processed] -> (p3)
CREATE(m9)-[r10:processed] -> (p3)
CREATE(m7)-[r11:processed] -> (p3)
CREATE(m10:Physical:Enginereed:EngineeredComponent:CatalysLayer {uid: randomUUID()})
CREATE(p3)-[r12:fabricates] -> (m10)
CREATE (p4:Physical:Process:Manufacturing {uid: randomUUID()})
CREATE(m10)-[r13:processed] -> (p4)
CREATE(c)-[r14:processed] -> (p4)
CREATE(c1)-[r15:processed] -> (p4)
CREATE(m12:Physical:Enginereed:EngineeredComponent:MEA {name: "MEA", type: "MEA"})
CREATE(p4)-[r16:fabricates] -> (m12)
MERGE (pa1:Physical:Process:Parameter {type: "HotPressed"})
CREATE(p4)-[r17:usesParameter {value: 1}] -> (pa1)
CREATE (p5:Physical:Process:Manufacturing {uid: randomUUID()})
CREATE(m12)-[r18:processed] -> (p5)
CREATE(c2)-[r19:processed] -> (p5)
CREATE(c3)-[r20:processed] -> (p5)
CREATE(p5)-[r21:fabricates] -> (d)
Merge (pa2:Physical:Process:Parameter {type: "I/C"})
CREATE (me:Physical:Process:Measurement {uid: randomUUID()})
CREATE(m10)-[r22:measured] -> (me)
CREATE(p3)-[r24:usesParameter {value: line.IC}] -> (pa2)
MERGE (pr:Physical:PhysicalDimension:Property {type: "PtLoading/cm2"})
CREATE(me)-[r25:yieldsQuant {value: line.Pt_loading_mgcm2geo}] -> (pr)

merge (pr31:Physical:PhysicalDimension:Property {type: "HOT"})
Merge (pr321:Physical:PhysicalDimension:Property {type: "NOC"})
merge (pr331:Physical:PhysicalDimension:Property {type: "WUP"})

CREATE (me21:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r261:measured] -> (me21)
CREATE(me21)-[r621:yieldsQuant {value: line.HOT_24_V}] -> (pr31)
MERGE (pa301:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me21)-[r2261:usesParameter{value: 2.4}] -> (pa301)

CREATE (me221:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2621:measured] -> (me221)
CREATE(me221)-[r6221:yieldsQuant {value: line.NOC_24_V}] -> (pr321)
MERGE (pa321:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me221)-[r22621:usesParameter{value: 2.4}] -> (pa321)

CREATE (me231:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2631:measured] -> (me231)
CREATE(me231)-[r6231:yieldsQuant {value: line.WUP_24_V}] -> (pr331)
MERGE (pa331:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me231)-[r22631:usesParameter{value: 2.4}] -> (pa331)

CREATE (me22:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r262:measured] -> (me22)
CREATE(me22)-[r622:yieldsQuant {value: line.HOT_24_V}] -> (pr31)
MERGE (pa302:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me22)-[r2262:usesParameter{value: 2.1}] -> (pa302)

CREATE (me222:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2622:measured] -> (me222)
CREATE(me222)-[r6222:yieldsQuant {value: line.NOC_24_V}] -> (pr321)
MERGE (pa322:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me222)-[r22622:usesParameter{value: 2.1}] -> (pa322)

CREATE (me232:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2632:measured] -> (me232)
CREATE(me232)-[r6232:yieldsQuant {value: line.WUP_24_V}] -> (pr331)
MERGE (pa332:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me232)-[r22632:usesParameter{value: 2.1}] -> (pa332)

CREATE (me23:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r263:measured] -> (me23)
CREATE(me23)-[r623:yieldsQuant {value: line.HOT_24_V}] -> (pr31)
MERGE (pa303:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me23)-[r2263:usesParameter{value: 1.9}] -> (pa303)

CREATE (me223:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2623:measured] -> (me223)
CREATE(me223)-[r6223:yieldsQuant {value: line.NOC_24_V}] -> (pr321)
MERGE (pa323:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me223)-[r22623:usesParameter{value: 1.9}] -> (pa323)

CREATE (me233:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2633:measured] -> (me233)
CREATE(me233)-[r6233:yieldsQuant {value: line.WUP_24_V}] -> (pr331)
MERGE (pa333:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me233)-[r22633:usesParameter{value: 1.9}] -> (pa333)

CREATE (me24:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r264:measured] -> (me24)
CREATE(me24)-[r624:yieldsQuant {value: line.HOT_24_V}] -> (pr31)
MERGE (pa304:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me24)-[r2264:usesParameter{value: 1.7}] -> (pa304)

CREATE (me224:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2624:measured] -> (me224)
CREATE(me224)-[r6224:yieldsQuant {value: line.NOC_24_V}] -> (pr321)
MERGE (pa324:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me224)-[r22624:usesParameter{value: 1.7}] -> (pa324)

CREATE (me234:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2634:measured] -> (me234)
CREATE(me234)-[r6234:yieldsQuant {value: line.WUP_24_V}] -> (pr331)
MERGE (pa334:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me234)-[r22634:usesParameter{value: 1.7}] -> (pa334)

CREATE (me25:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r265:measured] -> (me25)
CREATE(me25)-[r625:yieldsQuant {value: line.HOT_24_V}] -> (pr31)
MERGE (pa305:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me25)-[r2265:usesParameter{value: 1.5}] -> (pa305)

CREATE (me225:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2625:measured] -> (me225)
CREATE(me225)-[r6225:yieldsQuant {value: line.NOC_24_V}] -> (pr321)
MERGE (pa325:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me225)-[r22625:usesParameter{value: 1.5}] -> (pa325)

CREATE (me235:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2635:measured] -> (me235)
CREATE(me235)-[r6235:yieldsQuant {value: line.WUP_24_V}] -> (pr331)
MERGE (pa335:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me235)-[r22635:usesParameter{value: 1.5}] -> (pa335)

CREATE (me26:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r266:measured] -> (me26)
CREATE(me26)-[r626:yieldsQuant {value: line.HOT_24_V}] -> (pr31)
MERGE (pa306:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me26)-[r2266:usesParameter{value: 1.2}] -> (pa306)

CREATE (me226:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2626:measured] -> (me226)
CREATE(me226)-[r6226:yieldsQuant {value: line.NOC_24_V}] -> (pr321)
MERGE (pa326:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me226)-[r22626:usesParameter{value: 1.2}] -> (pa326)

CREATE (me236:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2636:measured] -> (me236)
CREATE(me236)-[r6236:yieldsQuant {value: line.WUP_24_V}] -> (pr331)
MERGE (pa336:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me236)-[r22636:usesParameter{value: 1.2}] -> (pa336)

CREATE (me27:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r267:measured] -> (me27)
CREATE(me27)-[r627:yieldsQuant {value: line.HOT_24_V}] -> (pr31)
MERGE (pa307:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me27)-[r2267:usesParameter{value: 1.0}] -> (pa307)

CREATE (me227:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2627:measured] -> (me227)
CREATE(me227)-[r6227:yieldsQuant {value: line.NOC_24_V}] -> (pr321)
MERGE (pa327:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me227)-[r22627:usesParameter{value: 1.0}] -> (pa327)

CREATE (me237:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2637:measured] -> (me237)
CREATE(me237)-[r6237:yieldsQuant {value: line.WUP_24_V}] -> (pr331)
MERGE (pa337:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me237)-[r22637:usesParameter{value: 1.0}] -> (pa337)

CREATE (me28:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r268:measured] -> (me28)
CREATE(me28)-[r628:yieldsQuant {value: line.HOT_24_V}] -> (pr31)
MERGE (pa308:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me28)-[r2268:usesParameter{value: 0.6}] -> (pa308)

CREATE (me228:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2628:measured] -> (me228)
CREATE(me228)-[r6228:yieldsQuant {value: line.NOC_24_V}] -> (pr321)
MERGE (pa328:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me228)-[r22628:usesParameter{value: 0.6}] -> (pa328)

CREATE (me238:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2638:measured] -> (me238)
CREATE(me238)-[r6238:yieldsQuant {value: line.WUP_24_V}] -> (pr331)
MERGE (pa338:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me238)-[r22638:usesParameter{value: 0.6}] -> (pa338)

CREATE (me29:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r269:measured] -> (me29)
CREATE(me29)-[r629:yieldsQuant {value: line.HOT_24_V}] -> (pr31)
MERGE (pa309:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me29)-[r2269:usesParameter{value: 0.2}] -> (pa309)

CREATE (me229:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2629:measured] -> (me229)
CREATE(me229)-[r6229:yieldsQuant {value: line.NOC_24_V}] -> (pr321)
MERGE (pa329:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me229)-[r22629:usesParameter{value: 0.2}] -> (pa329)

CREATE (me239:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r2639:measured] -> (me239)
CREATE(me239)-[r6239:yieldsQuant {value: line.WUP_24_V}] -> (pr331)
MERGE (pa339:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me239)-[r22639:usesParameter{value: 0.2}] -> (pa339)

CREATE (me2a1:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r26a1:measured] -> (me2a1)
CREATE(me2a1)-[r62a1:yieldsQuant {value: line.HOT_24_V}] -> (pr31)
MERGE (pa30a1:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me2a1)-[r226a1:usesParameter{value: 0.1}] -> (pa30a1)

CREATE (me22a1:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r262a1:measured] -> (me22a1)
CREATE(me22a1)-[r622a1:yieldsQuant {value: line.NOC_24_V}] -> (pr321)
MERGE (pa32a1:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me22a1)-[r2262a1:usesParameter{value: 0.1}] -> (pa32a1)

CREATE (me23a1:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r263a1:measured] -> (me23a1)
CREATE(me23a1)-[r623a1:yieldsQuant {value: line.WUP_24_V}] -> (pr331)
MERGE (pa33a1:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me23a1)-[r2263a1:usesParameter{value: 0.1}] -> (pa33a1)

CREATE (me2a2:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r26a2:measured] -> (me2a2)
CREATE(me2a2)-[r62a2:yieldsQuant {value: line.HOT_24_V}] -> (pr31)
MERGE (pa30a2:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me2a2)-[r226a2:usesParameter{value: 0.05}] -> (pa30a2)

CREATE (me22a2:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r262a2:measured] -> (me22a2)
CREATE(me22a2)-[r622a2:yieldsQuant {value: line.NOC_24_V}] -> (pr321)
MERGE (pa32a2:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me22a2)-[r2262a2:usesParameter{value: 0.05}] -> (pa32a2)

CREATE (me23a2:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r263a2:measured] -> (me23a2)
CREATE(me23a2)-[r623a2:yieldsQuant {value: line.WUP_24_V}] -> (pr331)
MERGE (pa33a2:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me23a2)-[r2263a2:usesParameter{value: 0.05}] -> (pa33a2)

CREATE (me2a3:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r26a3:measured] -> (me2a3)
CREATE(me2a3)-[r62a3:yieldsQuant {value: line.HOT_24_V}] -> (pr31)
MERGE (pa30a3:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me2a3)-[r226a3:usesParameter{value: 0}] -> (pa30a3)

CREATE (me22a3:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r262a3:measured] -> (me22a3)
CREATE(me22a3)-[r622a3:yieldsQuant {value: line.NOC_24_V}] -> (pr321)
MERGE (pa32a3:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me22a3)-[r2262a3:usesParameter{value: 0}] -> (pa32a3)

CREATE (me23a3:Physical:Process:Measurement {uid: randomUUID()})
CREATE(d)-[r263a3:measured] -> (me23a3)
CREATE(me23a3)-[r623a3:yieldsQuant {value: line.WUP_24_V}] -> (pr331)
MERGE (pa33a3:Physical:PhysicalDimension:Parameter {type: "Voltage"})
CREATE(me23a3)-[r2263a3:usesParameter{value: 0}] -> (pa33a3)


"""]

test = """
MERGE(ps:Process {Substrate: line.Transfer_substrate})
MERGE(m: Properties {name="Subjective_Crack_rating", value: line.Subjective_Crack_rating, type="Volumetric"})
MERGE(o: Process {name: "Hot_pressed", line.Hot_pressed})
MERGE(p: Physical:PhysicalDimension:Property {name: "", line.Hot_pressed})
MERGE(q: Process {substrate: line.Coating_substrate})
MERGE(r: Process {Time: line.Drymill_time_hrs})
MERGE(s: Process {Temp: line.Drying_temp_deg_C})
MERGE(t: Process {Name: line.Catalyst})
MERGE(u: Process {Name: line.Ionomer})
MERGE(pp: Process {Name: line.IC})
MERGE(pq: Process {Loading: line.Pt_loading_mgcm2geo})
MERGE(pr: Properties {Thickness: line.SEM_CCL_thickness_µm, unit: "micrometer"})
MERGE(pt: Properties {PV: line.Calculated_PV_based_on_SEM_thickness_cm3cm2geo})
MERGE(pu: Properties {PV: line.Calculated_porosity_based_on_SEM_thickness_, unit: "%"})
MERGE(pr)-[a:calculated_from] -> (pt)
MERGE(pr)-[b:calculated_from] -> (pu)
MERGE(n)-[c:has_property] -> (pr)
MERGE(n)-[d:used] -> (ps)
MERGE(n)-[r:has_property] -> (m)
MERGE(n)-[s:pressed_with] -> (o)
MERGE(n)-[t:coated_with] -> (p)
MERGE(n)-[u:drymilled_with] -> (q)
MERGE(n)-[v:dried_with] -> (nn)
MERGE(n)-[w:used_catalyst] -> (mm)
MERGE(n)-[x:used_solvant] -> (po)
MERGE(n)-[y:used_cat_iono_ratio] -> (pp)
MERGE(n)-[z:used_catalyst_loading] -> (pq)
"""
