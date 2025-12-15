import random

acne_guidance = {
    "Blackheads": {
        "advice": [
            "Avoid squeezing blackheads. Cleanse twice daily.",
            "Gently exfoliate 1-2 times per week. Avoid heavy creams.",
            "Maintain a consistent cleansing routine to prevent clogging."
        ],
        "cleanser": [
            ("CeraVe Foaming Cleanser", "https://www.cerave.com/skincare/cleansers/facial-cleansers/-acne-foaming-cream-wash-"),
            ("La Roche-Posay Effaclar Gel", "https://www.laroche-posay.us/our-products/face/acne-products/effaclar-medicated-acne-face-wash-effaclaracnewash.html"),
            ("Neutrogena Oil-Free Acne Wash", "https://www.neutrogena.com/products/skincare/oil-free-acne-wash-with-salicylic-acid/6801712")
        ],
        "moisturizer": [
            ("CeraVe Moisturizing Lotion", "https://www.cerave.com/skincare/moisturizers/daily-moisturizing-lotion"),
            ("Neutrogena Hydro Boost Gel", "https://www.neutrogena.com/products/skincare/neutrogena-hydro-boost-water-gel-with-hyaluronic-acid/6811047")
        ],
        "spot_treatment": [
            ("COSRX BHA Blackhead Power Liquid", "https://www.cosrx.com/products/bha-blackhead-power-liquid"),
            ("Paula's Choice 2% BHA", "https://www.paulaschoice.com/skin-perfecting-2-bha-liquid-exfoliant/201.html")
        ],
        "diet_tips": [
            "Reduce sugary foods and dairy.",
            "Eat more vegetables and hydrate well.",
            "Include omega-3 rich foods like salmon and walnuts."
        ],
        "lifestyle": [
            "Do not touch face frequently.",
            "Wash pillowcases weekly.",
            "Exercise regularly."
        ]
    },
    "Cyst": {
        "advice": [
            "Avoid squeezing or picking cysts. Consult a dermatologist for prescription treatments.",
            "Use gentle skincare products and avoid harsh scrubs.",
            "Maintain a consistent routine and avoid makeup on cysts."
        ],
        "cleanser": [
            ("La Roche-Posay Effaclar Gentle Cleanser", "https://www.laroche-posay.us/our-products/face/face-wash/toleriane-purifying-foaming-face-wash-tolerianepurifyingfoamingfacialwash.html?dwvar_tolerianepurifyingfoamingfacialwash_size=400ML"),
            ("Cetaphil Gentle Skin Cleanser", "https://www.cetaphil.com/us/products/product-categories/all-cleansers/gentle-skin-cleanser/302990110227.html")
        ],
        "moisturizer": [
            ("CeraVe Moisturizing Cream", "https://www.cerave.com/skincare/moisturizers/moisturizing-cream"),
            ("Neutrogena Hydro Boost Gel", "https://www.neutrogena.com/products/skincare/neutrogena-hydro-boost-water-gel-with-hyaluronic-acid/6811047")
        ],
        "spot_treatment": [
            ("Differin Adapalene Gel", "https://www.target.com/p/differin-acne-retinoid-treatment-gel-adapalene-0-1-15g/-/A-51346324?sid=64S&TCID=PDS-336245569&gclsrc=aw.ds&gad_source=1&gad_campaignid=336245569&gbraid=0AAAAAD-5dfaDetWZZcMVuAXDjLHABFEh3&gclid=CjwKCAiA3fnJBhAgEiwAyqmY5d42eAyNftSsnUEkOKutdCaQene8sOOSy2AriwBvkcrIrkHxyya_LRoCeN0QAvD_BwE"),
            ("Benzac AC Gel", "https://www.target.com/p/differin-10-bpo-spot-treatment/-/A-91370206?sid=64S&TCID=PDS-336245569&gclsrc=aw.ds&gad_source=1&gad_campaignid=336245569&gbraid=0AAAAAD-5dfaDetWZZcMVuAXDjLHABFEh3&gclid=CjwKCAiA3fnJBhAgEiwAyqmY5S0KYQyludX9jBX7iqoHgG3rhfmbq5jivATBsvJ4x4dgkEbUS3FvTRoCtvIQAvD_BwE")
        ],
        "diet_tips": [
            "Limit dairy and high glycemic index foods.",
            "Include more omega-3 rich foods like flaxseeds and fish.",
            "Drink plenty of water and green tea."
        ],
        "lifestyle": [
            "Keep skin clean and avoid makeup on cysts.",
            "Manage stress through meditation or yoga.",
            "Do not pick or squeeze the cysts."
        ]
    },
    "Papules": {
        "advice": [
            "Treat early with topical benzoyl peroxide or salicylic acid.",
            "Maintain gentle skin routine and avoid harsh scrubs.",
            "Do not pick or squeeze papules to prevent scarring."
        ],
        "cleanser": [
            ("Neutrogena Rapid Clear", "https://ctchealth.ca/product/neutrogena-rapid-clear-stubborn-acne-facial-cleanser-benzoyl-peroxide-acne-treatment-face-wash-125ml/?gad_source=1&gad_campaignid=13954660242&gbraid=0AAAAADEtuoPyKE1glKGju7v8tU6WSzFG7&gclid=CjwKCAiA3fnJBhAgEiwAyqmY5eQWu59yffotNkI47Qo50CaTxzs7ju10H66dZiWb3sCxjq47_cj0choCnakQAvD_BwE"),
            ("Cetaphil Gentle Cleanser", "https://www.cetaphil.com/us/products/product-categories/all-cleansers/gentle-skin-cleanser/302990110227.html")
    
        ],
        "moisturizer": [
            ("CeraVe Moisturizing Lotion", "https://www.cerave.com/skincare/moisturizers/daily-moisturizing-lotion"),
            ("La Roche-Posay Toleriane", "https://www.laroche-posay.us/our-products/face/face-moisturizer/toleriane-double-repair-face-moisturizer-tolerianedoublerepair.html")
        ],
        "spot_treatment": [
            ("Benzac AC Gel", "https://www.target.com/p/differin-10-bpo-spot-treatment/-/A-91370206?sid=64S&TCID=PDS-336245569&gclsrc=aw.ds&gad_source=1&gad_campaignid=336245569&gbraid=0AAAAAD-5dfaDetWZZcMVuAXDjLHABFEh3&gclid=CjwKCAiA3fnJBhAgEiwAyqmY5S0KYQyludX9jBX7iqoHgG3rhfmbq5jivATBsvJ4x4dgkEbUS3FvTRoCtvIQAvD_BwE"),
            ("Paula's Choice 2% BHA", "https://www.paulaschoice.com/skin-perfecting-2-bha-liquid-exfoliant/201.html")
        ],
        "diet_tips": [
            "Increase fruits and vegetables, reduce fried and processed foods.",
            "Limit sugary beverages and snacks.",
            "Include foods rich in zinc and vitamin A."
        ],
        "lifestyle": [
            "Avoid touching face and clean makeup brushes regularly.",
            "Ensure adequate sleep and manage stress.",
            "Wash pillowcases weekly."
        ]
    },
    "Pustules": {
        "advice": [
            "Spot treat pustules and avoid picking.",
            "Use gentle cleansing and moisturizing routine.",
            "Maintain consistent skincare to prevent new pustules."
        ],
        "cleanser": [
            ("Cetaphil Gentle Cleanser", "https://www.cetaphil.com/us/products/product-categories/all-cleansers/gentle-skin-cleanser/302990110227.html"),
             ("Neutrogena Oil-Free Acne Wash", "https://www.neutrogena.com/products/skincare/oil-free-acne-wash-with-salicylic-acid/6801712")
        ],
        "moisturizer": [
            ("CeraVe Moisturizing Lotion", "https://www.cerave.com/skincare/moisturizers/daily-moisturizing-lotion"),
           ("Neutrogena Hydro Boost Gel", "https://www.neutrogena.com/products/skincare/neutrogena-hydro-boost-water-gel-with-hyaluronic-acid/6811047")
        ],
        "spot_treatment": [
            ("Paula's Choice 2% BHA", "https://www.paulaschoice.com/skin-perfecting-2-bha-liquid-exfoliant/201.html"),
            ("COSRX Centella Blemish Cream", "https://www.cosrx.com/products/centella-blemish-cream")
        ],
        "diet_tips": [
            "Reduce sugar, processed foods, and dairy.",
            "Hydrate well and eat more green vegetables.",
            "Include probiotics like yogurt or kefir."
        ],
        "lifestyle": [
            "Do not pop pustules, wash pillowcases weekly.",
            "Limit touching face and keep hair away from face.",
            "Exercise regularly and manage stress."
        ]
    },
    "Whiteheads": {
        "advice": [
            "Use gentle exfoliation and non-comedogenic moisturizers.",
            "Avoid heavy creams and maintain a simple skincare routine.",
            "Do not pick or squeeze whiteheads."
        ],
        "cleanser": [
             ("Cerave Foaming Cleanser", "https://www.target.com/p/cerave-foaming-face-wash-with-hyaluronic-acid-and-niacinamide-for-oily-skin-8-fl-oz/-/A-76198441?sid=64S&TCID=PDS-336245569&gclsrc=aw.ds&gad_source=1&gad_campaignid=336245569&gbraid=0AAAAAD-5dfaDetWZZcMVuAXDjLHABFEh3&gclid=CjwKCAiA3fnJBhAgEiwAyqmY5dPSYIqskHTFXiNJ06DfGYx8WQ7OyYelRJ9SByKBg-5WxwSih_0nrxoCxu4QAvD_BwE"),
            ("La Roche-Posay Effaclar Gel", "https://www.target.com/p/la-roche-posay-toleriane-purifying-facial-cleanser-with-niacinamide-for-oily-skin-13-52-fl-oz/-/A-51195574?sid=64S&TCID=PDS-336245569&gclsrc=aw.ds&gad_source=1&gad_campaignid=336245569&gbraid=0AAAAAD-5dfaDetWZZcMVuAXDjLHABFEh3&gclid=CjwKCAiA3fnJBhAgEiwAyqmY5ayFL5HjzGHDfuoa3tko9_WWxYuWdXKchCPiHpXnCq_TE24vAU-KzhoCKfQQAvD_BwE")
        ],
        "moisturizer": [
            ("CeraVe Moisturizing Lotion", "https://www.cerave.com/skincare/moisturizers/daily-moisturizing-lotion"),
           ("Neutrogena Hydro Boost Gel", "https://www.neutrogena.com/products/skincare/neutrogena-hydro-boost-water-gel-with-hyaluronic-acid/6811047")
        ],
        "spot_treatment": [
            ("Paula's Choice 2% BHA", "https://www.paulaschoice.com/skin-perfecting-2-bha-liquid-exfoliant/201.html"),
            ("COSRX BHA Whitehead Power Liquid", "https://www.yesstyle.com/en/tcuc.USD/coc.US/info.html/pid.1052684699?cpid=1052684698&googtrans=en&utm_source=GoogleAds&utm_campaign=1424525216&utm_term=&utm_content=54082139977_274225508780&utm_medium=Shopping&bac=MIEU1SGQ&mcg=paidsearch&gad_source=1&gad_campaignid=1424525216&gbraid=0AAAAAD3WTkk7VK9bq1RTofTHcTb3PMV1m&gclid=CjwKCAiA3fnJBhAgEiwAyqmY5ZwnefA_kr-RkI3Pe7OFXk0-t7ZHXTEq5e8dpFW5KCdTJs_rAW6bFBoClvkQAvD_BwE")
        ],
        "diet_tips": [
            "Eat more leafy vegetables and protein.",
            "Avoid sugary snacks and fried foods.",
            "Drink plenty of water and herbal teas."
        ],
        "lifestyle": [
            "Keep skin routine consistent and wash hands frequently.",
            "Avoid touching face and clean pillowcases regularly.",
            "Exercise and manage stress effectively."
        ]
    }
}

def get_items(items, n=2):
    """Pick n random items from a list"""
    return random.sample(items, min(len(items), n))

def get_acne_recommendation(acne_type):
    info = acne_guidance.get(acne_type, {})
    rec = {
        "advice": random.choice(info.get("advice", [])),
        "cleanser": get_items(info.get("cleanser", [])),
        "moisturizer": get_items(info.get("moisturizer", [])),
        "spot_treatment": get_items(info.get("spot_treatment", [])),
        "diet_tips": random.choice(info.get("diet_tips", [])),
        "lifestyle": random.choice(info.get("lifestyle", []))
    }
    return rec
