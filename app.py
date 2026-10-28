import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='FisioDigestivo IA', page_icon='🧠', layout='wide', initial_sidebar_state='collapsed')

st.markdown('''
<style>
.block-container{padding-top:1.1rem;padding-bottom:1.5rem;max-width:1200px}.author{text-align:center;color:#667085;font-size:.82rem;padding-top:1.2rem}
.hero{background:linear-gradient(135deg,#F4FBF7 0%,#EEF7FF 100%);border:1px solid #DCE8E3;border-radius:18px;padding:16px 18px;margin-bottom:.7rem}.hero-title{font-size:1.7rem;font-weight:850;color:#17324D}.hero-sub{font-size:.98rem;color:#52606d}
.stTabs [data-baseweb="tab-list"]{gap:.28rem!important;background:transparent!important;padding:.35rem 0 0!important;border-bottom:2px solid rgba(80,100,120,.16)!important;align-items:flex-end!important}.stTabs [data-baseweb="tab"]{position:relative!important;border-radius:12px 12px 0 0!important;border:1px solid rgba(50,70,90,.20)!important;border-bottom:none!important;padding:.58rem .82rem .52rem!important;min-height:44px!important;font-weight:800!important;color:#18324a!important;top:2px!important}.stTabs [data-baseweb="tab"]:nth-child(1){background:#A7D8F0!important}.stTabs [data-baseweb="tab"]:nth-child(2){background:#B9E4C9!important}.stTabs [data-baseweb="tab"]:nth-child(3){background:#F7D6A6!important}.stTabs [data-baseweb="tab"]:nth-child(4){background:#D9C5F0!important}.stTabs [data-baseweb="tab"]:nth-child(5){background:#F7B9C5!important}.stTabs [data-baseweb="tab"]::before{content:""!important;position:absolute!important;top:-7px!important;left:10px!important;width:42%!important;height:8px!important;border-radius:7px 7px 0 0!important;background:inherit!important;border:1px solid rgba(50,70,90,.16)!important;border-bottom:none!important}.stTabs [aria-selected="true"]{top:0!important;filter:saturate(1.08) brightness(1.02)!important;box-shadow:0 -2px 8px rgba(0,0,0,.10)!important;border-width:2px!important;z-index:2!important}.stTabs [data-baseweb="tab-highlight"]{display:none!important}
.card{border:1px solid #E0E7EC;border-radius:14px;padding:12px 14px;background:#fff;margin-bottom:10px}.step{border-left:5px solid #78B7C5;padding:10px 12px;background:#F8FBFD;border-radius:10px;margin-bottom:8px}.accessory{border:1px solid #E5DDD2;background:#FFFDF8;border-radius:14px;padding:12px;margin-bottom:10px}.tag{display:inline-block;padding:3px 8px;border-radius:999px;font-size:.78rem;font-weight:700;margin-right:5px}.tag-blue{background:#E3F2FD;color:#0D47A1}.tag-green{background:#E8F5E9;color:#1B5E20}.tag-orange{background:#FFF3E0;color:#E65100}.tag-purple{background:#F3E5F5;color:#4A148C}.quizbox{border:1px solid #DDE5EB;border-radius:14px;padding:12px 14px;background:#FAFCFD;margin-bottom:10px}.correct{background:#E8F5E9;border:1px solid #A5D6A7;border-radius:10px;padding:8px 10px}.incorrect{background:#FFEBEE;border:1px solid #FFCDD2;border-radius:10px;padding:8px 10px}.explain{background:#FFF8E1;border:1px solid #FFE082;border-radius:10px;padding:8px 10px;margin-top:6px}
@media(max-width:760px){.block-container{padding-left:.65rem;padding-right:.65rem;padding-top:.8rem}.hero{padding:12px 13px}.hero-title{font-size:1.35rem}.stTabs [data-baseweb="tab-list"]{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:.38rem!important;border-bottom:none!important;padding-top:.45rem!important}.stTabs [data-baseweb="tab"]{width:100%!important;justify-content:center!important;border-radius:12px!important;border:1px solid rgba(50,70,90,.20)!important;top:0!important;padding:.55rem .4rem!important;font-size:.88rem!important;white-space:normal!important}.stTabs [data-baseweb="tab"]::before{display:none!important}}
</style>
''', unsafe_allow_html=True)

st.markdown('''<div class="hero"><div class="hero-title">FisioDigestivo IA</div><div class="hero-sub">Anatomía funcional del sistema digestivo · recorrido, órganos accesorios y aplicación clínica sencilla</div></div>''', unsafe_allow_html=True)

tab1,tab2,tab3,tab4,tab5=st.tabs(['Recorrido digestivo','Órganos y funciones','Órganos accesorios','Viaje del alimento','Práctica'])

with tab1:
    st.subheader('Recorrido digestivo')
    st.caption('Sigue el trayecto del alimento y relaciona cada segmento con su función principal.')
    recorrido=[('Boca','Ingestión, trituración, mezcla con saliva y formación del bolo alimenticio.'),('Faringe','Participa en la deglución y comunica la cavidad oral con el esófago.'),('Esófago','Conduce el bolo al estómago mediante movimientos peristálticos.'),('Estómago','Mezcla el bolo con jugo gástrico y forma el quimo.'),('Duodeno','Recibe quimo, bilis y jugo pancreático; inicia digestión química intensa.'),('Yeyuno','Principal sitio de absorción de azúcares, aminoácidos, vitaminas y minerales.'),('Íleon','Absorbe vitamina B12 y sales biliares; se conecta con el ciego.'),('Intestino grueso','Absorbe agua y electrolitos y participa en la formación de las heces.'),('Recto y ano','Almacenamiento transitorio de heces y eliminación al exterior.')]
    for i,(org,fun) in enumerate(recorrido,1): st.markdown(f'<div class="step"><b>{i}. {org}</b><br>{fun}</div>',unsafe_allow_html=True)
    st.info('Funciones generales: ingestión, secreción, mezcla y propulsión, digestión, absorción y defecación.')

with tab2:
    st.subheader('Órganos y funciones'); st.caption('Relaciona estructura y función antes de pasar a la aplicación clínica.')
    c1,c2=st.columns(2)
    with c1:
        st.markdown('<div class="card"><h4>Boca y glándulas salivales</h4><span class="tag tag-blue">Saliva</span><span class="tag tag-green">Amilasa salival</span><p>Mantienen húmeda la mucosa, lubrican el alimento, comienzan la digestión de almidones y contribuyen al gusto y lavado de la cavidad oral.</p></div>',unsafe_allow_html=True)
        st.markdown('<div class="card"><h4>Esófago</h4><span class="tag tag-purple">Peristaltismo</span><p>Conduce el bolo hasta el estómago. Presenta esfínter esofágico superior e inferior.</p></div>',unsafe_allow_html=True)
        st.markdown('<div class="card"><h4>Estómago</h4><span class="tag tag-orange">Quimo</span><p>Recibe el bolo, lo mezcla con jugo gástrico y forma quimo. Presenta cardias, fondo, cuerpo, antro y canal pilórico.</p></div>',unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><h4>Intestino delgado</h4><span class="tag tag-blue">Duodeno</span><span class="tag tag-green">Yeyuno</span><span class="tag tag-purple">Íleon</span><p>Principal lugar de absorción de nutrientes. El duodeno recibe bilis y jugo pancreático; yeyuno e íleon completan la absorción.</p></div>',unsafe_allow_html=True)
        st.markdown('<div class="card"><h4>Intestino grueso</h4><span class="tag tag-green">Agua</span><span class="tag tag-blue">Electrolitos</span><p>Absorbe agua y electrolitos y participa en la formación y conducción de las heces.</p></div>',unsafe_allow_html=True)
        st.markdown('<div class="card"><h4>Recto</h4><span class="tag tag-orange">Ampolla rectal</span><p>Almacena transitoriamente las heces. El canal anal presenta un esfínter interno involuntario y uno externo voluntario.</p></div>',unsafe_allow_html=True)
    st.markdown('#### Peritoneo')
    st.markdown('<div class="card">Posee hoja <b>parietal</b> y <b>visceral</b>. Sus repliegues incluyen <b>mesenterios, ligamentos y omentos</b>. Entre sus funciones se describen sostén, movimiento de vísceras, protección, aislamiento térmico e intercambio.</div>',unsafe_allow_html=True)

with tab3:
    st.subheader('Órganos accesorios'); st.caption('Hígado, vesícula biliar y páncreas.')
    a,b,c=st.columns(3)
    with a: st.markdown('<div class="accessory"><h4>Hígado</h4><p>Glándula mayor del organismo. Almacena glucógeno y produce bilis.</p><b>Pedículo hepático:</b><br>vena porta + arteria hepática + conducto hepático.</div>',unsafe_allow_html=True)
    with b: st.markdown('<div class="accessory"><h4>Vesícula biliar</h4><p>Concentra y almacena bilis.</p><p>La expulsa hacia el duodeno durante la digestión.</p></div>',unsafe_allow_html=True)
    with c: st.markdown('<div class="accessory"><h4>Páncreas</h4><p>Glándula mixta.</p><b>Exocrina:</b> jugo pancreático.<br><b>Endocrina:</b> insulina y glucagón.</div>',unsafe_allow_html=True)
    st.markdown('#### Trayecto de la bilis')
    st.markdown('<div class="step"><b>Conductos hepáticos derecho e izquierdo</b> → conducto hepático común</div><div class="step"><b>Conducto cístico</b> + conducto hepático común → colédoco</div><div class="step"><b>Colédoco</b> se relaciona con el conducto pancreático y llega al duodeno</div>',unsafe_allow_html=True)
    st.markdown('#### Sistema porta hepático')
    st.markdown('<div class="card">Conduce sangre desde el tracto gastrointestinal hacia el hígado a través de la vena porta. Esta sangre es pobre en O₂ y rica en nutrientes absorbidos.</div>',unsafe_allow_html=True)

with tab4:
    st.subheader('Viaje del alimento'); st.caption('Selecciona un segmento y observa qué recibe, qué ocurre allí y qué continúa después.')
    organos={
        'Boca':('Alimentos','Trituración, mezcla con saliva e inicio de digestión de almidones.','Bolo alimenticio hacia la faringe.'),
        'Esófago':('Bolo alimenticio','Transporte mediante peristaltismo.','Bolo hacia el estómago.'),
        'Estómago':('Bolo alimenticio','Mezcla con jugo gástrico y formación de quimo.','Quimo hacia el duodeno a través del píloro.'),
        'Duodeno':('Quimo + bilis + jugo pancreático','Digestión química intensa de grasas, proteínas y carbohidratos.','Contenido hacia yeyuno.'),
        'Yeyuno':('Contenido intestinal parcialmente digerido','Absorción importante de azúcares, aminoácidos, vitaminas y minerales.','Contenido hacia íleon.'),
        'Íleon':('Contenido proveniente del yeyuno','Absorción de vitamina B12 y sales biliares.','Contenido hacia el ciego mediante la válvula ileocecal.'),
        'Intestino grueso':('Contenido desde el íleon','Absorción de agua y electrolitos y formación de heces.','Heces hacia recto.')}
    elegido=st.selectbox('Selecciona una estación del recorrido',list(organos.keys()))
    recibe,ocurre,sale=organos[elegido]
    st.markdown(f'<div class="card"><h4>{elegido}</h4><p><b>Recibe:</b> {recibe}</p><p><b>Qué ocurre:</b> {ocurre}</p><p><b>Qué sigue:</b> {sale}</p></div>',unsafe_allow_html=True)
    components.html('''<style>.route{display:flex;align-items:center;gap:6px;overflow-x:auto;padding:8px 4px 12px}.node{min-width:88px;text-align:center;padding:9px 7px;border-radius:12px;background:#F3F7FB;border:1px solid #D9E3EA;font-family:Arial;font-size:11px;font-weight:700}.arrow{font-size:18px;color:#6B7C8F}</style><div class="route"><div class="node">Boca</div><div class="arrow">→</div><div class="node">Faringe</div><div class="arrow">→</div><div class="node">Esófago</div><div class="arrow">→</div><div class="node">Estómago</div><div class="arrow">→</div><div class="node">Duodeno</div><div class="arrow">→</div><div class="node">Yeyuno</div><div class="arrow">→</div><div class="node">Íleon</div><div class="arrow">→</div><div class="node">Colon</div><div class="arrow">→</div><div class="node">Recto</div></div>''',height=95,scrolling=False)

with tab5:
    st.subheader('Práctica'); st.caption('Tres tandas progresivas con retroalimentación breve.')
    tandas=st.tabs(['🔵 Tanda 1 · Fundamentos','🟢 Tanda 2 · Aplicación','🟠 Tanda 3 · Clínica'])
    preguntas1=[
        ('¿Cuál es la función principal del esófago?',['Absorber agua','Conducir el bolo al estómago','Producir bilis','Formar heces'],'Conducir el bolo al estómago','El esófago transporta el bolo desde la faringe hasta el estómago mediante peristaltismo.'),
        ('¿Dónde se forma el quimo?',['Boca','Esófago','Estómago','Colon'],'Estómago','El quimo se forma cuando el bolo se mezcla con el jugo gástrico.'),
        ('¿Cuál es el principal sitio de absorción de nutrientes?',['Intestino delgado','Esófago','Recto','Faringe'],'Intestino delgado','El intestino delgado es el principal lugar donde se absorben nutrientes.'),
        ('¿Qué estructura almacena transitoriamente las heces?',['Fondo gástrico','Ampolla rectal','Duodeno','Vesícula biliar'],'Ampolla rectal','La ampolla rectal almacena temporalmente las heces antes de la defecación.'),
        ('¿Qué estructura inicia la digestión de almidones mediante amilasa salival?',['Glándulas salivales','Hígado','Páncreas endocrino','Vesícula biliar'],'Glándulas salivales','La saliva contiene amilasa salival y participa en el inicio de la digestión de almidones.')]
    preguntas2=[
        ('¿Qué segmento recibe quimo, bilis y jugo pancreático?',['Yeyuno','Duodeno','Íleon','Colon ascendente'],'Duodeno','El duodeno recibe quimo del estómago, bilis y jugo pancreático.'),
        ('¿Qué segmento se asocia a absorción de vitamina B12 y sales biliares?',['Íleon','Yeyuno','Duodeno','Recto'],'Íleon','La clase identifica al íleon como sitio de absorción de vitamina B12 y sales biliares.'),
        ('La unión del conducto cístico con el conducto hepático común forma:',['Conducto pancreático','Colédoco','Conducto hepático derecho','Conducto de Santorini'],'Colédoco','El conducto cístico y el hepático común forman el colédoco.'),
        ('¿Qué componente del páncreas corresponde a su función digestiva?',['Secreción exocrina','Secreción endocrina','Producción de glucógeno','Almacenamiento de bilis'],'Secreción exocrina','La función exocrina pancreática corresponde a la liberación de jugo pancreático.'),
        ('¿Qué sistema transporta sangre rica en nutrientes desde el tubo digestivo hacia el hígado?',['Sistema porta hepático','Circulación pulmonar','Sistema linfático exclusivamente','Circulación coronaria'],'Sistema porta hepático','La vena porta conduce sangre proveniente del tracto gastrointestinal hacia el hígado.')]
    preguntas3=[
        ('Una persona presenta dificultad para que el bolo avance desde la faringe hasta el estómago. ¿Qué estructura debe evaluarse prioritariamente?',['Esófago','Colon sigmoide','Vesícula biliar','Íleon'],'Esófago','El esófago es el conducto que lleva el bolo hacia el estómago mediante peristaltismo.'),
        ('Una alteración compromete la salida del quimo desde el estómago al duodeno. ¿Qué estructura está más directamente relacionada?',['Píloro','Cardias','Válvula ileocecal','Esfínter anal externo'],'Píloro','El píloro regula el paso del contenido gástrico hacia el duodeno.'),
        ('Un paciente presenta mala absorción de vitamina B12 y sales biliares. ¿Qué segmento intestinal se relaciona más con este problema?',['Íleon','Yeyuno','Duodeno','Colon transverso'],'Íleon','Según la clase, el íleon participa en la absorción de vitamina B12 y sales biliares.'),
        ('Una alteración disminuye la absorción de agua y electrolitos al final del tubo digestivo. ¿Qué órgano participa principalmente en esa función?',['Intestino grueso','Estómago','Esófago','Faringe'],'Intestino grueso','El intestino grueso absorbe agua y electrolitos y participa en la formación de las heces.'),
        ('Una obstrucción impide el paso normal de bilis hacia el duodeno. ¿Qué conducto lleva finalmente la bilis en esa dirección?',['Colédoco','Conducto de Santorini','Conducto hepático derecho','Vena porta'],'Colédoco','El colédoco se forma a partir del conducto hepático común y el conducto cístico y continúa hacia el duodeno.'),
        ('Una lesión afecta la función digestiva del páncreas, pero mantiene la secreción de insulina y glucagón. ¿Qué componente está comprometido?',['Función exocrina','Función endocrina','Vesícula biliar','Sistema porta'],'Función exocrina','La secreción digestiva pancreática corresponde a la función exocrina.'),
        ('Después de la absorción intestinal, la sangre rica en nutrientes debe llegar primero al hígado. ¿Qué sistema lo permite?',['Sistema porta hepático','Aorta torácica','Sistema pulmonar','Sistema linfático superficial'],'Sistema porta hepático','El sistema porta conduce la sangre desde el tracto gastrointestinal hacia el hígado.')]
    def mostrar(lista,prefijo):
        for i,(q,opts,a,e) in enumerate(lista,1):
            key=f'{prefijo}_{i}'
            st.markdown(f'<div class="quizbox"><b>{i}. {q}</b></div>',unsafe_allow_html=True)
            resp=st.radio(f'Respuesta {i}',opts,index=None,key=key,label_visibility='collapsed')
            if st.button('Responder',key=f'btn_{key}'):
                if resp is None: st.warning('Selecciona una alternativa antes de responder.')
                elif resp==a:
                    st.markdown('<div class="correct"><b>Correcto.</b></div>',unsafe_allow_html=True); st.markdown(f'<div class="explain"><b>¿Por qué?</b> {e}</div>',unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="incorrect"><b>Incorrecto.</b> La respuesta correcta es: {a}.</div>',unsafe_allow_html=True); st.markdown(f'<div class="explain"><b>¿Por qué?</b> {e}</div>',unsafe_allow_html=True)
            st.markdown('---')
    with tandas[0]:
        st.markdown('### Tanda 1 de 3 · Fundamentos'); st.caption('Reconocimiento de estructuras y funciones.'); mostrar(preguntas1,'Fundamentos')
    with tandas[1]:
        st.markdown('### Tanda 2 de 3 · Aplicación'); st.caption('Relaciones funcionales y trayectos.'); mostrar(preguntas2,'Aplicación')
    with tandas[2]:
        st.markdown('### Tanda 3 de 3 · Clínica'); st.caption('Casos breves centrados en estructura y función.'); mostrar(preguntas3,'Clinica')

st.markdown('<div class="author">Creado por Cristian Barahona Videla · Uso educativo · © 2026</div>',unsafe_allow_html=True)
