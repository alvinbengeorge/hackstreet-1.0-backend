# -*- coding: utf-8 -*-
from Questgen import main
from time import time
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

import nltk

nltk.download("stopwords")
print("Importing Model")
answer = main.AnswerPredictor()
qg = main.QGen()
print("Imported Model")

def generateFAQ(text: str):
    result = []
    questions = [i["Question"] for i in qg.predict_shortq({"input_text": text})['questions']][:3]
    for question in questions:
        result.append(
            {
                "question": question,
                "answer": answerQuestion(text, question)
            }
        )
    print(result)
    return result

def generateSummary(text: str):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    stemmer = Stemmer("english")
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words("english")
    return " ".join([str(sentence) for sentence in summarizer(parser.document, 7)])

def answerQuestion(text: str, question: str):
    payload = {
        "input_text": text,
        "input_question": question,
    }
    startTime = time()
    payload = answer.predict_answer(payload)
    print(time() - startTime)
    return payload


if __name__ == "__main__":
    print(*generateFAQ("Bone tuberculosis affects your skeletal system, including your bones and joints. Spinal tuberculosis is the most prevalent form of bone tuberculosis which occurs when your spinal cord becomes infected with Mycobacterium. Pott's illness is another name for spinal TB.Bone tuberculosis is prevalent in developing nations and is among the top 10 global killers [1]. Bone TB is uncommon but difficult to diagnose and, if neglected, can have serious consequences.Types of TuberculosisExtrapulmonary tuberculosis describes TB when it spreads (EPTB) to other areas such as the abdomen, skin, joints, etc. Tuberculosis of the bones and joints is one type of EPTB. The spine, long bones, and joints are all affected by bone tuberculosisTuberculosis of the lungs is often known as pulmonary tuberculosis. The infection may result in lung issues, breathing difficulties, and chest painWhat Causes Bone Tuberculosis?Sometimes, tuberculosis can spread to your bones and cause bone TB. TB can also spread between people through airborne transmission. The disease can spread from the lymph nodes or lungs into the bones, spine, or joints once you develop tuberculosis. Bone TB frequently develops in the dense vascular supply in the middle of the long bones and vertebrae.The long bones are particularly vulnerable to tuberculous infection, which are similar to benign tumours, locally aggressive tumours like giant cell tumours, and occasionally even malignant tumours like osteogenic sarcoma or chondrosarcomas. As a result, it leads to bone cancer.List of Factors that May Cause Bone TuberculosisIncorrect treatmentThe illness may spread to your lungs and other organs if you are not diagnosed on time. Therefore, appropriate care is needed before the situation worsens. Early signs of bone TB are noticeable and should be treated as soon as possible.TransmissionIt is an infectious illness that spreads swiftly from one person to another. Once it enters the human body, it will affect the lungs, lymph nodes, thymus, and bones. Therefore, patients should recognise the symptoms and signs of bone TB to begin therapy as soon as possible. Patients with a history of active TB are more likely to develop osteoporosis and experience bone fractures.  It\u00e2\u20ac\u2122s essential to check our bone health periodically.Additional Read: Leg Fracture: Symptoms and Treatments\u00c2\u00a0Types of Bone TBBone tuberculosis can affect you in many different forms, such as: \tUpper extremity tuberculosis \tAnkle joint tuberculosis \tKnee joint tuberculosis \tElbow tuberculosis \tHip joint tuberculosis \tSpinal tuberculosisSymptoms of Bone TuberculosisBone TB, mainly spinal TB, is painless in the early stages, and the patient may not display any symptoms making it difficult to detect. However, the signs and symptoms of bone TB are typically fairly advanced when it is ultimately detected.In rare cases, the illness can lie latent in the lungs and spread without the patient knowing they have any tuberculosis. However, there are a few signs to look out for if a patient has developed bone TB: \tBack and joint stiffness \tInflamed joints \tBack pain that is severe and ongoing \tBone pain \tAbnormal blood loss \tAppetite loss \tOngoing fever, especially one of low grade \tExtreme chills \tSweating at night, feeling exhausted all the time \tCough with blood \tSharp chest ache \tA strong, three- or longer-lasting coughWhen your condition is at an advanced stage, other symptoms will manifest. The following are the signs of advanced bone TB: \tBone malformations \tLimb shortening in children \tParalysis \tNeurological issuesAdditional Read: Scoliosis: Causes, SymptomsTreatment for Bone TuberculosisBone tuberculosis has a high mortality rate if untreated.However, bone tuberculosis damage can be reversed using the following treatments:MedicinesAnti-tuberculosis medications include rifampicin, streptomycin, kanamycin, isoniazid, prothionamide, cycloserine, and pyrazinamide. They can go inside the cerebral fluid and start fighting the germs. The recovery from bone TB may take six to twelve monthsCorticosteroidsThese drugs may be recommended to avoid issues, including inflammation around the heart or spinal cordMDRAntitubercular medications are taken as part of MDR treatment. It is the most advantageous course of treatment to get rid of the symptoms in the boneDOTS TreatmentDirect Observed Treatment is another name for it. Patients with signs of bone TB are strongly advised to take itSurgerySurgery may be required to remove an infected portion if you have advanced bone tuberculosisDiagnosis of Bone TuberculosisIt is frequently diagnosed using the following techniques:Bacterial cultivationYou most likely have a lung infection if you have bone tuberculosis. Your doctor may take a sample of your blood or sputum for testing for Mycobacterium tuberculosis.BiopsyYour physician would prescribe a biopsy, which entails removing a sample of affected tissue and testing it for infection. Bone marrow biopsy can help test for spinal TB lesions.Examination of bodily fluidsTo examine your lungs for infections, your doctor may take a sample of the pleural fluid surrounding and protecting them. For example, they could remove cerebrospinal fluid from the region surrounding your spinal cord or synovial or joint fluid for testing to check for bone or joint TB.\u00e2\u20ac\u00afComplications of Bone TuberculosisAlthough spinal TB is uncommon (1\u00e2\u20ac\u201c3% of the time), it is a disorder that can be fatal once discovered. The severity might increase the longer it remains untreated. In addition, the severity might increase the longer it remains untreated. Typical difficulties include: \tVertebral collapse resulting in back rounding or bending (kyphosis) \tCompressed spinal cord \tThe development of a cold abscess in the cervical area \tSevere infection that might spread to the mediastinum or trachea and other areas and possibly result in the creation of sinuses \tSevere neurological issues \tNo movement in the lower bodyAdditional Read: Spinal Cord Injury DayBone tuberculosis poses a greater danger in developing countries. Although the threat of TB is reduced in affluent countries, bone tuberculosis is nevertheless a concern. Drugs can be used to treat this condition once it has been recognised, and in more complex situations, medication can be used in combination with surgical intervention.Visit Bajaj Finserv Health to get a doctor consultation if you experience any bone TB symptoms or have more queries."), sep="\n\n")

