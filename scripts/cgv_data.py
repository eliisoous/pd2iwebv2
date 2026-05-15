# -*- coding: utf-8 -*-
"""Structured CGV / General Terms of Sale content for FR, EN, ZH."""

META = {
    "fr": {
        "title": "Conditions générales de vente | PD2i",
        "description": "Conditions générales de vente PD2i : commandes, livraisons, prix, garanties et droit applicable.",
        "hero_title": "Conditions générales de vente",
        "hero_sub": "Modalités contractuelles applicables aux ventes de produits PD2i aux professionnels",
        "hero_badge": "📋 CGV professionnelles",
        "breadcrumb": "Conditions générales de vente",
        "last_updated": "Dernière mise à jour : janvier 2026",
        "contact_title": "Questions sur les CGV ?",
        "contact_text": "Pour toute question relative aux présentes conditions générales de vente, contactez-nous.",
        "contact_btn": "Nous contacter",
        "contact_or": "Ou par e-mail :",
        "console_msg": "Page CGV chargée",
    },
    "en": {
        "title": "General Terms of Sale | PD2i",
        "description": "PD2i general terms of sale: orders, deliveries, pricing, warranties, and governing law.",
        "hero_title": "General Terms of Sale",
        "hero_sub": "Contractual terms applicable to PD2i product sales to business customers",
        "hero_badge": "📋 Business terms",
        "breadcrumb": "General Terms of Sale",
        "last_updated": "Last updated: January 2026",
        "contact_title": "Questions about these terms?",
        "contact_text": "If you have any questions regarding these general terms of sale, please contact us.",
        "contact_btn": "Contact us",
        "contact_or": "Or by email:",
        "console_msg": "General terms of sale page loaded",
    },
    "zh": {
        "title": "销售条款与条件 | PD2i",
        "description": "PD2i 销售条款与条件：订单、交货、价格、保证及适用法律。",
        "hero_title": "销售条款与条件",
        "hero_sub": "适用于 PD2i 向专业客户销售产品的合同约定",
        "hero_badge": "📋 商务销售条款",
        "breadcrumb": "销售条款与条件",
        "last_updated": "最后更新：2026年1月",
        "contact_title": "对销售条款有疑问？",
        "contact_text": "若对本销售条款与条件有任何疑问，请与我们联系。",
        "contact_btn": "联系我们",
        "contact_or": "或发送电子邮件至：",
        "console_msg": "销售条款页面已加载",
    },
}

# Each entry: (article_heading, list of paragraph strings)
ARTICLES_FR = [
    (
        "ARTICLE 1 – Champ d'application",
        [
            "1.1- Toutes nos relations contractuelles sont soumises exclusivement aux présentes conditions générales de vente (CGV). Sauf acceptation expresse et écrite du Vendeur, les conditions générales d'achat dérogatoires ou clauses contraires émanant du client ne peuvent prévaloir sur les présentes CGV.",
            "1.2- Nos produits sont exclusivement destinés à des professionnels qui reconnaissent avoir pleinement connaissance des risques inhérents à leurs usages.",
            "1.3- La renonciation expresse éventuelle de notre part à une ou plusieurs clauses figurant aux présentes conditions générales est sans incidence sur la validité des autres clauses qui demeurent applicables entre les parties.",
            "1.4- Le fait de passer une commande implique l'adhésion entière et sans réserve de l'Acheteur aux présentes CGV.",
        ],
    ),
    (
        "ARTICLE 2 – Commandes",
        [
            "2.1- Chaque contrat de vente ne sera formé que lors de l'acceptation de la commande sous la forme d'un accusé de réception établi par nos soins fixant l'étendue de la fourniture des produits. En raison des problèmes de chaîne d'approvisionnement causés par la crise logistique mondiale, les tensions et pénuries d'énergie et de matières premières, malgré nos meilleurs efforts, des modifications ou annulations du contrat de vente peuvent survenir.",
            "2.2- Toute commande peut être composée de livraisons différentes, successives ou partielles. Toutes les livraisons devront être considérées comme constituant des ventes distinctes dont un retard ou un défaut n'affecteront pas les autres parties de la commande.",
        ],
    ),
    (
        "ARTICLE 3 – Livraisons",
        [
            "3.1- Nos livraisons sont faites en fonction de nos disponibilités. Sauf convention expresse, nos délais de livraison indicatifs sont de 5 à 10 jours ouvrés. Compte tenu de la livraison « sortie usine », notre société n'est pas responsable des éventuels retards liés au transport. L'Acheteur ne pourra se prévaloir d'un retard pour annuler sa commande, refuser les produits ou réclamer des dommages et intérêts.",
            "3.2- En cas de livraisons successives, le défaut, l'insuffisance ou le retard d'une livraison sont sans incidence sur les autres livraisons.",
            "3.3- Sous réserve d'un accord écrit contraire, les produits sont livrés « sortie usine (Ex Works) » tel que ce terme est défini dans les Incoterms 2020.",
        ],
    ),
    (
        "ARTICLE 4 – Prix",
        [
            "Les prix facturés seront ceux de la commande. Toute modification des charges fiscales ou douanières incombant au Vendeur, survenue après l'acceptation de la commande, entraînera une variation correspondante du prix convenu, avec un préavis écrit de deux (2) mois. Pour le cas où le prix aurait été fixé en fonction du cours des matières premières ou des devises utilisées, les variations desdits cours ne pourront être en aucun cas un motif de résiliation de la commande. Sauf stipulations contraires, nos prix s'entendent hors taxe, nets de tout escompte, hors coût de transport, d'emballage, de droits d'importation, de frais de douane et d'assurance. Ces frais seront facturés en sus. Les paiements seront effectués dans la devise facturée.",
        ],
    ),
    (
        "ARTICLE 5 – Poids et quantités",
        [
            "Pour toutes les ventes, quelle qu'en soit la destination, les poids et quantités figurant sur les documents d'expédition (bon de livraison, lettre de voiture, connaissement maritime…) seront seuls pris en considération pour l'établissement des factures.",
        ],
    ),
    (
        "ARTICLE 6 – Tolérances",
        [
            "Il est toléré une variation de 10% en plus ou en moins par rapport à la commande sur les quantités livrées ou sur les poids, lesdites variations étant naturellement toujours facturées.",
        ],
    ),
    (
        "ARTICLE 7 – Étiquetage – Réglementation REACH",
        [
            "7.1- L'Acheteur s'engage à se référer et à respecter la réglementation européenne relative à l'enregistrement, l'évaluation, et l'autorisation des substances chimiques (Règlement CE n°1907/2006 du 18 décembre 2006 – « Règlement REACH »). Nos produits sont tous étiquetés et emballés conformément à la réglementation européenne en vigueur applicable aux ventes à des professionnels.",
            "7.2- L'acceptation de toute offre émanant de notre société implique de la part du client la reconnaissance du respect de cette réglementation. Dans l'hypothèse où l'Acheteur souhaite revendre nos produits au grand public, il lui incombe de vérifier si cela est possible compte tenu de leur composition et de les rendre conformes aux réglementations applicables, notamment pour l'étiquetage, l'emballage et le marquage. L'Acheteur tient le Vendeur à l'abri des actions ou demandes à ce titre.",
        ],
    ),
    (
        "ARTICLE 8 – Transport des produits",
        [
            "Le transport des produits doit respecter la réglementation européenne en vigueur relative au transport des matières dangereuses. En conséquence, l'acheteur fera en sorte que le transport des produits respecte ladite réglementation. Lorsque l'Acheteur organise le transport vers l'étranger, il transmet obligatoirement au Vendeur tous les justificatifs de livraison signés ainsi que, dans les délais requis, tous les documents visés à l'article 45 bis du Règlement UE n°282/2011.",
        ],
    ),
    (
        "ARTICLE 9 – Transfert des risques",
        [
            "9.1- Le transfert des risques liés aux produits (perte, détérioration, avaries…) se fait à la livraison « sortie usine ». Toutes les ventes sont concernées, quelle que soit leur pays de destination et quelles que soient les modalités de vente ou de transport, et ce compte tenu de la livraison sortie usine (Ex Works) des produits.",
            "9.2- Les produits voyagent aux risques et périls de l'Acheteur, en ce compris les opérations de transport, assurance, douane et manutention. Il appartient donc à l'Acheteur de vérifier les expéditions à leur arrivée et d'exercer s'il y a lieu les recours contre le transporteur. En cas de manquant, d'avarie (dommage, bris, destruction, perte…) ou de retard, le destinataire doit faire lui-même toutes les réserves qu'il jugera utiles auprès du transporteur responsable dans les délais et formes imposés par la loi, en particulier dans les délais prévus à l'article L. 133-3 du Code de Commerce français (3 jours) sous peine de perdre irrévocablement tout recours contre celui-ci.",
        ],
    ),
    (
        "ARTICLE 10 – Contestation",
        [
            "Sous réserve des contestations faites au Transporteur qui doivent être effectuées conformément aux dispositions de l'article 9, toute contestation sur les quantités livrées et/ou sur leur conformité à la commande devra être formulée par écrit dans un délai de 8 jours suivant la livraison Sortie Usine (Ex Works) des produits. Les réclamations concernant la qualité devront être également formulées par écrit dans le même délai. En cas de réclamation régulièrement formulée et justifiée, nous avons le choix entre l'échange des produits ou leur reprise au prix facturé, à l'exclusion de toute autre indemnité. Aucun retour ne pourra être fait sans accord préalable.",
        ],
    ),
    (
        "ARTICLE 11 – Réserve de propriété",
        [
            "11.1- De convention expresse entre les parties, les produits livrés ne deviennent propriété définitive de l'Acheteur qu'après paiement effectif et complet du prix et de ses accessoires.",
            "11.2- En conséquence, le Vendeur pourra, sans mise en demeure préalable, exiger de l'Acheteur la restitution des produits impayés dans les délais.",
            "11.3- L'Acheteur s'interdit d'enlever les emballages ou étiquettes des produits existants en nature dans ses stocks et non encore réglés, et à les assurer à ses frais contre les risques de perte et de détérioration.",
            "11.4- Conformément aux articles L. 624-9 et suivants du code de commerce, le Vendeur a un droit de revendication sur les produits vendus avec une clause de réserve de propriété s'ils se trouvent en nature dans le patrimoine du débiteur au moment de l'ouverture d'une procédure de redressement judiciaire ou de liquidation judiciaire, ou de toute procédure équivalente.",
        ],
    ),
    (
        "ARTICLE 12 – Conditions de paiement – Pénalités",
        [
            "12.1- L'Acheteur transmet au Vendeur un numéro d'identification aux fins de la TVA dont il garantit la validité.",
            "12.2- Nos factures sont payables à 30 jours net à compter de la date d'émission de la facture, par virement bancaire. Le paiement est réputé effectué au siège social de notre société et à la date à laquelle notre compte bancaire est crédité. Le Vendeur a la possibilité de compenser toute somme due par l'Acheteur et impayée avec toute somme due par le Vendeur à l'Acheteur. En cas de retard de paiement, une pénalité de retard sera due, calculée sur la base d'un taux égal à trois fois le taux d'intérêt légal. En outre, une indemnité forfaitaire de 40 euros sera facturée pour frais de recouvrement. Le défaut de paiement à l'échéance de toute somme due entraînera l'exigibilité immédiate de toutes les sommes restant dues. Le Vendeur se réserve la faculté de les suspendre ou de les résoudre de plein droit.",
        ],
    ),
    (
        "ARTICLE 13 – Garanties – Responsabilité",
        [
            "13.1- Notre société ne pourra en aucun cas être tenue pour responsable des conséquences d'une utilisation fautive ou non conforme à la prudence et aux usages, compte tenu de la nature des produits et des dangers qu'ils peuvent présenter pour l'environnement et la santé, en particulier en cas de leur dispersion accidentelle ; ceci concerne aussi la manipulation, le stockage ou le transport des produits vendus.",
        ],
    ),
    (
        "ARTICLE 14 – Données personnelles",
        [
            "Le Vendeur collecte et traite les données personnelles des interlocuteurs de l'Acheteur nécessaires à la gestion de la relation commerciale, conformément au RGPD n°2016/679. Ces données sont conservées pendant la durée de la relation commerciale augmentée des délais légaux applicables. Pour exercer vos droits, contactez : admin@pd2i.com.",
        ],
    ),
    (
        "ARTICLE 15 – Force majeure",
        [
            "En cas de survenance d'un événement constitutif de force majeure, les obligations seront suspendues aussi longtemps que durera la force majeure. Au-delà de six mois, les ventes et/ou commandes seront résolues de plein droit.",
        ],
    ),
    (
        "ARTICLE 16 – Loi applicable – Juridiction compétente",
        [
            "16.1- Tout différend relatif à ou résultant de l'interprétation, l'exécution ou la résiliation des présentes CGV et/ou de toute vente sera soumis au droit français et aux dispositions de la Convention de Vienne sur la vente internationale de produits du 11 avril 1980.",
            "16.2- En cas de contestation quelconque relative à l'interprétation, à l'exécution ou la résiliation des présentes CGV et/ou de toute vente, le Tribunal de Commerce de Paris sera seul compétent pour connaître de toute demande (tant au principal qu'en intervention ou en garantie) et ce, même s'il y a pluralité de défendeurs ou appels incidents.",
        ],
    ),
]

FOOTER_LINE_FR = (
    "CONDITIONS GÉNÉRALES DE VENTE | PD2-I – SAS au capital de [CAPITAL] € – RCS Paris 451 239 800 – N° TVA FR22451239800 — "
    "Siège Social : 86 Boulevard Malesherbes, 75008 Paris | Tél : +33 (0)1 53 75 45 05 | admin@pd2i.com | https://pd2i.com"
)

ARTICLES_EN = [
    (
        "ARTICLE 1 – Scope of application",
        [
            "1.1 All our contractual relationships are governed exclusively by these General Terms of Sale (GTS). Unless the Seller has expressly accepted them in writing, the Buyer's conflicting or derogatory general purchasing conditions may not prevail over these GTS.",
            "1.2 Our products are intended exclusively for professionals who acknowledge that they are fully aware of the risks inherent in their use.",
            "1.3 Any express waiver by us of one or more clauses of these GTS shall not affect the validity of the remaining clauses, which shall continue to apply between the parties.",
            "1.4 Placing an order implies the Buyer's full and unreserved acceptance of these GTS.",
        ],
    ),
    (
        "ARTICLE 2 – Orders",
        [
            "2.1 Each sale contract is formed only upon acceptance of the order in the form of an acknowledgement of receipt issued by us, defining the scope of the product supply. Due to supply-chain issues arising from the global logistics crisis, energy and raw-material tensions and shortages, modifications or cancellations of the sale contract may occur despite our best efforts.",
            "2.2 Any order may consist of separate, successive or partial deliveries. Each delivery shall be treated as a distinct sale; delay or default on one delivery shall not affect other parts of the order.",
        ],
    ),
    (
        "ARTICLE 3 – Deliveries",
        [
            "3.1 Deliveries are made subject to availability. Unless otherwise agreed, indicative delivery times are 5 to 10 business days. As delivery is 'ex-works', our company is not liable for any transport-related delays. The Buyer may not rely on delay to cancel the order, refuse the products or claim damages.",
            "3.2 In the case of successive deliveries, default, shortfall or delay on one delivery shall not affect the other deliveries.",
            "3.3 Unless otherwise agreed in writing, products are delivered 'ex works (Ex Works)' as defined in Incoterms 2020.",
        ],
    ),
    (
        "ARTICLE 4 – Prices",
        [
            "Invoiced prices shall be those stated in the order. Any change in taxes or customs charges borne by the Seller after order acceptance shall result in a corresponding adjustment of the agreed price, with two (2) months' prior written notice. Where the price was set with reference to raw-material or currency rates, fluctuations in such rates may not in any event be grounds for cancelling the order. Unless otherwise stated, our prices are exclusive of tax, without any cash discount, and exclude transport, packaging, import duties, customs fees and insurance; such costs will be invoiced separately. Payments shall be made in the invoiced currency.",
        ],
    ),
    (
        "ARTICLE 5 – Weights and quantities",
        [
            "For all sales, whatever the destination, only the weights and quantities shown on shipping documents (delivery note, consignment note, bill of lading, etc.) shall be used for invoicing.",
        ],
    ),
    (
        "ARTICLE 6 – Tolerances",
        [
            "A tolerance of plus or minus 10% on quantities delivered or weights compared with the order is allowed; such variations shall always be invoiced.",
        ],
    ),
    (
        "ARTICLE 7 – Labelling – REACH regulation",
        [
            "7.1 The Buyer undertakes to refer to and comply with European legislation on the registration, evaluation and authorisation of chemicals (Regulation (EC) No 1907/2006 of 18 December 2006 – 'REACH'). Our products are all labelled and packaged in accordance with the European regulations applicable to sales to professionals.",
            "7.2 Acceptance of any offer from our company implies the customer's acknowledgement of compliance with this regulation. If the Buyer wishes to resell our products to consumers, it is responsible for verifying feasibility in view of their composition and for ensuring compliance with applicable regulations, in particular for labelling, packaging and marking. The Buyer shall hold the Seller harmless from any claims in this respect.",
        ],
    ),
    (
        "ARTICLE 8 – Transport of products",
        [
            "Transport of the products must comply with applicable European rules on the transport of dangerous goods. Accordingly, the Buyer shall ensure that transport complies with those rules. Where the Buyer arranges transport abroad, it must send the Seller all signed proof-of-delivery documents and, within the required time limits, all documents referred to in Article 45 bis of EU Regulation No 282/2011.",
        ],
    ),
    (
        "ARTICLE 9 – Transfer of risk",
        [
            "9.1 Risk relating to the products (loss, deterioration, damage, etc.) passes at 'ex-works' delivery. This applies to all sales, whatever the country of destination and whatever the sale or transport terms, given ex-works (Ex Works) delivery of the products.",
            "9.2 Products travel at the Buyer's risk, including transport, insurance, customs and handling. The Buyer must therefore inspect shipments on arrival and, where appropriate, pursue claims against the carrier. In case of shortage, damage (breakage, destruction, loss, etc.) or delay, the consignee must itself make any reservations it deems necessary with the liable carrier within the time limits and formalities required by law, in particular within the period provided for in Article L. 133-3 of the French Commercial Code (3 days), failing which any remedy against the carrier shall be irrevocably lost.",
        ],
    ),
    (
        "ARTICLE 10 – Disputes on delivery",
        [
            "Subject to claims against the carrier which must be made in accordance with Article 9, any dispute concerning quantities delivered and/or their conformity with the order must be notified in writing within 8 days of ex-works (Ex Works) delivery. Quality claims must likewise be made in writing within the same period. Where a claim is duly made and justified, we may choose between replacing the products or taking them back at the invoiced price, to the exclusion of any other compensation. No return may be made without prior agreement.",
        ],
    ),
    (
        "ARTICLE 11 – Retention of title",
        [
            "11.1 It is expressly agreed between the parties that delivered products shall become the Buyer's property only after full payment of the price and related charges.",
            "11.2 Accordingly, the Seller may, without prior formal notice, require the Buyer to return unpaid products within the stated time limits.",
            "11.3 The Buyer shall not remove packaging or labels from products still in stock and not yet paid for, and shall insure them at its own expense against loss and damage.",
            "11.4 In accordance with Articles L. 624-9 et seq. of the French Commercial Code, the Seller has a right to reclaim products sold with a retention-of-title clause if they are still identifiable in the debtor's estate at the opening of reorganisation, liquidation or any equivalent proceedings.",
        ],
    ),
    (
        "ARTICLE 12 – Payment terms – Penalties",
        [
            "12.1 The Buyer shall provide the Seller with a valid VAT identification number and warrants its accuracy.",
            "12.2 Our invoices are payable net 30 days from the invoice date by bank transfer. Payment is deemed made at our registered office on the date our bank account is credited. The Seller may set off any unpaid amount due from the Buyer against any amount the Seller owes the Buyer. In case of late payment, late-payment interest shall accrue at three times the statutory interest rate. A fixed recovery charge of EUR 40 shall also be invoiced. Failure to pay any amount when due shall render all remaining amounts immediately due. The Seller may suspend performance or terminate contracts by operation of law.",
        ],
    ),
    (
        "ARTICLE 13 – Warranties – Liability",
        [
            "13.1 Our company shall in no event be liable for consequences of faulty use or use inconsistent with reasonable care and trade practice, given the nature of the products and the risks they may pose to the environment and health, in particular in the event of accidental release; this also applies to handling, storage or transport of the products sold.",
        ],
    ),
    (
        "ARTICLE 14 – Personal data",
        [
            "The Seller collects and processes personal data of the Buyer's contacts as necessary to manage the commercial relationship, in accordance with GDPR No 2016/679. Data are kept for the duration of the relationship plus applicable statutory periods. To exercise your rights, contact: admin@pd2i.com.",
        ],
    ),
    (
        "ARTICLE 15 – Force majeure",
        [
            "If an event of force majeure occurs, obligations shall be suspended for as long as the force majeure continues. If it lasts more than six months, the sales and/or orders shall be terminated by operation of law.",
        ],
    ),
    (
        "ARTICLE 16 – Governing law – Jurisdiction",
        [
            "16.1 Any dispute relating to or arising from the interpretation, performance or termination of these GTS and/or any sale shall be governed by French law and the United Nations Convention on Contracts for the International Sale of Goods of 11 April 1980.",
            "16.2 Any dispute concerning the interpretation, performance or termination of these GTS and/or any sale shall fall within the exclusive jurisdiction of the Paris Commercial Court for all claims (on the merits, by intervention or warranty), even where there are multiple defendants or incidental claims.",
        ],
    ),
]

FOOTER_LINE_EN = (
    "GENERAL TERMS OF SALE | PD2-I – SAS with share capital of [CAPITAL] EUR – RCS Paris 451 239 800 – VAT No. FR22451239800 — "
    "Registered office: 86 Boulevard Malesherbes, 75008 Paris | Tel: +33 (0)1 53 75 45 05 | admin@pd2i.com | https://pd2i.com"
)

ARTICLES_ZH = [
    (
        "第1条 – 适用范围",
        [
            "1.1 我们的一切合同关系均仅受本销售条款与条件（以下简称“本条款”）约束。未经卖方明确书面同意，买方提出的与之相抵触或减损的采购一般条件不得优于本条款。",
            "1.2 我们的产品仅面向专业人士；专业人士确认其已充分了解产品使用所固有的风险。",
            "1.3 我方对本条款中一项或多项条款的任何明示放弃，不影响其余条款的效力，其余条款在双方之间继续适用。",
            "1.4 下订单即表示买方毫无保留地完全接受本条款。",
        ],
    ),
    (
        "第2条 – 订单",
        [
            "2.1 每份销售合同仅在我方以订单确认/回执形式接受订单、并确定供货范围时成立。鉴于全球物流危机、能源及原材料紧张与短缺造成的供应链问题，尽管我方已尽最大努力，仍可能出现销售合同的变更或取消。",
            "2.2 任何订单均可由不同、分批或多次的交付组成。每次交付应视为独立销售；其中一次交付的迟延或瑕疵不影响订单其他部分。",
        ],
    ),
    (
        "第3条 – 交付",
        [
            "3.1 交付视我方供货情况而定。除另有约定外，指示性交货期为5至10个工作日。鉴于采用“工厂交货”，本公司对运输可能造成的迟延不承担责任。买方不得以迟延为由取消订单、拒收产品或主张损害赔偿。",
            "3.2 如为连续交付，其中一次交付的瑕疵、数量不足或迟延不影响其他交付。",
            "3.3 除另有书面约定外，产品按《国际贸易术语解释通则2020》所定义的工厂交货（Ex Works）方式交付。",
        ],
    ),
    (
        "第4条 – 价格",
        [
            "发票价格以订单为准。在订单接受之后，如卖方承担的税费或关税发生变更，应在提前两（2）个月书面通知的情况下，对约定价格作相应调整。如价格系参照原材料或所用货币行情确定，则该等行情波动在任何情况下均不构成解除订单的理由。除另有说明外，我们的价格为不含税净价，不含任何现金折扣，亦不含运输、包装、进口税、关税及保险费；该等费用将另行计费。付款应以发票所列货币进行。",
        ],
    ),
    (
        "第5条 – 重量与数量",
        [
            "对于任何销售，无论目的地为何，发票仅以运输单据（送货单、运单、海运提单等）上所载重量与数量为准。",
        ],
    ),
    (
        "第6条 – 公差",
        [
            "就交付数量或重量而言，相对订单允许上下浮动10%；该等差异将照常计费。",
        ],
    ),
    (
        "第7条 – 标签与REACH法规",
        [
            "7.1 买方承诺查阅并遵守欧盟关于化学品注册、评估、授权和限制的法规（2006年12月18日第1907/2006号法规——“REACH法规”）。我们所有产品的标签与包装均符合适用于向专业人士销售的现行欧洲法规。",
            "7.2 接受我方任何报价即表示客户确认遵守该法规。如买方拟将产品再销售给消费者，其应自行核实是否可行，并确保在标签、包装及标识等方面符合适用法规。买方应使卖方免受与此相关的任何索赔。",
        ],
    ),
    (
        "第8条 – 产品运输",
        [
            "产品运输必须符合欧盟关于危险品运输的现行法规。因此，买方应确保运输符合该法规。如买方安排跨境运输，其必须向我方传送所有经签署的交付证明文件，并在规定期限内传送欧盟第282/2011号法规第45条之二所述的全部文件。",
        ],
    ),
    (
        "第9条 – 风险转移",
        [
            "9.1 与产品相关的风险（灭失、损坏、货损等）在“工厂交货”时转移。鉴于产品为工厂交货（Ex Works），无论目的地国家为何，也无论销售或运输方式如何，本条适用于所有销售。",
            "9.2 产品运输的风险由买方承担，包括运输、保险、海关及搬运作业。因此，买方应在到货时查验托运货物，并在必要时向承运人主张权利。如发生短少、货损（破损、毁灭、灭失等）或迟延，收货人应自行在法律规定的方式与期限内向责任承运人作出其认为必要的一切保留，特别是应在《法国商法典》第L.133-3条规定的期限内（3日）作出，否则将丧失对承运人的一切追索权。",
        ],
    ),
    (
        "第10条 – 异议",
        [
            "在不影响依第9条向承运人提出异议的前提下，对交付数量及/或其与订单一致性的任何异议，应在产品工厂交货（Ex Works）之日起8日内以书面提出。质量异议亦应在同一期限内以书面提出。如异议按规定提出且理由成立，我们可选择更换产品或按发票价格收回产品，不承担任何其他赔偿。未经事先同意，不得退货。",
        ],
    ),
    (
        "第11条 – 所有权保留",
        [
            "11.1 双方明确约定，所交付产品在价款及其从属费用全部实际支付之前，不构成买方最终所有。",
            "11.2 因此，卖方可在无事先催告的情况下，要求买方在期限内返还未付款产品。",
            "11.3 买方不得拆除其库存中尚未付款的在存产品的包装或标签，并应自费就该等产品投保灭失与损坏风险。",
            "11.4 依据《法国商法典》第L.624-9条及后续条款，如附所有权保留条款销售的产品在债务人进入司法重整、司法清算或任何同等程序之时仍可在其财产中以具体物辨别，卖方享有追及权。",
        ],
    ),
    (
        "第12条 – 付款条件与违约金",
        [
            "12.1 买方应向卖方提供用于增值税目的的识别号，并保证其真实有效。",
            "12.2 我们的发票应自开票日起30日净期以银行转账支付。付款视为于我方公司住所、并在款项记入我方银行账户之日完成。卖方可将买方到期未付款项与卖方对买方的应付款项进行抵销。如迟延付款，应按法定利率三倍的利率计收迟延利息。此外，将收取40欧元的固定催收费。任何到期未付款将导致所有余款立即到期。卖方可中止履行或依法解除合同。",
        ],
    ),
    (
        "第13条 – 保证与责任",
        [
            "13.1 对于因不当使用或未按谨慎义务及行业惯例使用产品而产生的后果，考虑到产品性质及其可能对环境与健康造成的危险（特别是意外泄漏情形），本公司概不负责；本条亦适用于所售产品的搬运、储存或运输。",
        ],
    ),
    (
        "第14条 – 个人数据",
        [
            "卖方根据欧盟第2016/679号条例（GDPR）收集并处理买方联系人管理商业关系所必需的个人数据。该等数据在商业关系存续期间及法定保存期限届满前予以保存。如需行使权利，请联系：admin@pd2i.com。",
        ],
    ),
    (
        "第15条 – 不可抗力",
        [
            "如发生不可抗力事件，相关义务在不可抗力持续期间中止。如超过六个月，相关销售及/或订单将依法当然解除。",
        ],
    ),
    (
        "第16条 – 适用法律与管辖",
        [
            "16.1 因本条款及/或任何销售的解释、履行或终止引起或与之相关的争议，适用法国法律及1980年4月11日《联合国国际货物销售合同公约》。",
            "16.2 因本条款及/或任何销售的解释、履行或终止引起的任何争议，由巴黎商事法院专属管辖（包括主诉、参加之诉或担保之诉），即使存在多名被告或附带请求亦然。",
        ],
    ),
]

FOOTER_LINE_ZH = (
    "销售条款与条件 | PD2-I – SAS，注册资本 [CAPITAL] 欧元 – 巴黎RCS 451 239 800 – 增值税号 FR22451239800 — "
    "注册地址：86 Boulevard Malesherbes, 75008 Paris | 电话：+33 (0)1 53 75 45 05 | admin@pd2i.com | https://pd2i.com"
)


def build_main_html(lang: str) -> str:
    if lang == "fr":
        articles, footer_line = ARTICLES_FR, FOOTER_LINE_FR
        m = META["fr"]
    elif lang == "zh":
        articles, footer_line = ARTICLES_ZH, FOOTER_LINE_ZH
        m = META["zh"]
    else:
        articles, footer_line = ARTICLES_EN, FOOTER_LINE_EN
        m = META["en"]

    blocks = []
    blocks.append(
        f'''
        <section class="hero-background py-12 text-white flex items-center min-h-[300px]">
            <div class="container mx-auto px-4">
                <div class="text-center text-white relative z-10">
                    <h1 class="text-3xl md:text-4xl font-bold mb-4 animate-fade-in">{m["hero_title"]}</h1>
                    <p class="text-lg md:text-xl mb-6 opacity-90 leading-relaxed max-w-4xl mx-auto animate-fade-in delay-200">{m["hero_sub"]}</p>
                    <div class="mt-8 animate-fade-in delay-400">
                        <div class="inline-block bg-white/10 backdrop-blur-sm rounded-lg p-6">
                            <p class="text-lg font-medium">{m["hero_badge"]}</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''
    )

    for i, (h2, paras) in enumerate(articles):
        bg = "bg-white" if i % 2 == 0 else "bg-gray-50"
        inner = "".join(
            f'<p class="text-gray-700 leading-relaxed mb-4 text-justify">{p}</p>' for p in paras
        )
        blocks.append(
            f'''
        <section class="py-12 {bg}">
            <div class="container mx-auto px-4">
                <div class="max-w-4xl mx-auto">
                    <div class="legal-card scroll-animate">
                        <h2 class="text-xl md:text-2xl font-bold text-pd2i-blue mb-6">{h2}</h2>
                        {inner}
                    </div>
                </div>
            </div>
        </section>'''
        )

    blocks.append(
        f'''
        <section class="py-12 bg-white">
            <div class="container mx-auto px-4">
                <div class="max-w-4xl mx-auto">
                    <div class="legal-card scroll-animate info-box">
                        <p class="text-sm text-gray-700 leading-relaxed">{footer_line}</p>
                    </div>
                </div>
            </div>
        </section>'''
    )

    blocks.append(
        f'''
        <section class="py-16 bg-gray-50">
            <div class="container mx-auto px-4">
                <div class="max-w-4xl mx-auto text-center">
                    <div class="legal-card scroll-animate">
                        <h2 class="text-2xl font-bold text-pd2i-blue mb-6">{m["contact_title"]}</h2>
                        <p class="text-gray-700 leading-relaxed mb-8">{m["contact_text"]}</p>
                        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                            <a href="contacts.html" class="contact-btn">{m["contact_btn"]}</a>
                            <div class="text-gray-600">
                                <p class="text-sm">{m["contact_or"]} <a href="mailto:admin@pd2i.com" class="text-pd2i-blue hover:underline">admin@pd2i.com</a></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''
    )

    blocks.append(
        f'''
        <section class="py-8 bg-gray-50 border-t border-gray-200">
            <div class="container mx-auto px-4">
                <div class="text-center text-gray-600 text-sm">
                    <p>{m["last_updated"]}</p>
                </div>
            </div>
        </section>'''
    )

    return "\n".join(blocks)
