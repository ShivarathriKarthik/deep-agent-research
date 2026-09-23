import streamlit as st
from pipeline import run_research_pipeline


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Deep Agent",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background: #0b0f14;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    /* Remove excessive top spacing */
    header {
        visibility: hidden;
    }

    /* Main title */
    .main-title {
        font-size: 32px;
        font-weight: 800;
        color: white;
        margin-bottom: 2px;
    }

    .main-subtitle {
        color: #8b949e;
        font-size: 13px;
        margin-bottom: 25px;
    }

    /* Input section */
    .research-box {
        background: #11161d;
        border: 1px solid #29313d;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 15px;
    }

    .research-title {
        color: white;
        font-size: 20px;
        font-weight: 700;
    }

    .research-description {
        color: #8b949e;
        font-size: 13px;
        margin-top: 6px;
    }

    /* Pipeline */
    .pipeline-wrapper {
        background: #10151c;
        border: 1px solid #29313d;
        border-radius: 18px;
        padding: 18px;
        margin-top: 0px;
    }

    .pipeline-heading {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 18px;
    }

    .pipeline-heading-text {
        color: white;
        font-size: 15px;
        font-weight: 700;
    }

    .ready-badge {
        background: rgba(34,197,94,0.10);
        color: #22c55e;
        border: 1px solid rgba(34,197,94,0.25);
        border-radius: 20px;
        padding: 4px 9px;
        font-size: 9px;
        font-weight: 700;
    }

    .agent-card {
        background: #151b23;
        border: 1px solid #27303b;
        border-radius: 12px;
        padding: 12px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .agent-icon {
        width: 36px;
        height: 36px;
        border-radius: 10px;
        background: #202733;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 17px;
    }

    .agent-name {
        color: #ffffff;
        font-size: 12px;
        font-weight: 700;
    }

    .agent-tool {
        color: #737e8d;
        font-size: 10px;
        margin-top: 2px;
    }

    .agent-number {
        margin-left: auto;
        color: #566170;
        font-size: 10px;
    }

    .pipeline-line {
        width: 2px;
        height: 12px;
        background: #303846;
        margin-left: 29px;
    }

    /* Architecture */
    .architecture {
        margin-top: 15px;
        padding: 15px;
        background: #0c1117;
        border: 1px solid #232b35;
        border-radius: 13px;
    }

    .architecture-title {
        color: white;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .architecture-flow {
        color: #7d8794;
        font-size: 10px;
        line-height: 1.9;
    }

    .architecture-flow span {
        color: #a78bfa;
    }

    /* Result header */
    .result-title {
        color: white;
        font-size: 21px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 4px;
    }

    .result-topic {
        color: #737e8d;
        font-size: 12px;
        margin-bottom: 15px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #4b5563;
        font-size: 11px;
        margin-top: 40px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

st.html(
    """
    <div style="
        display:flex;
        align-items:center;
        gap:14px;
        margin-bottom:5px;
    ">

        <div style="
            width:48px;
            height:48px;
            border-radius:14px;
            background:linear-gradient(135deg,#6366f1,#8b5cf6);
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:25px;
            box-shadow:0 0 25px rgba(99,102,241,0.25);
        ">
            🧠
        </div>

        <div>

            <div style="
                color:#ffffff;
                font-size:30px;
                font-weight:800;
                letter-spacing:-0.8px;
            ">
                Deep Agent
            </div>

            <div style="
                color:#8b949e;
                font-size:13px;
            ">
                Multi-Agent Research Intelligence System
            </div>

        </div>

    </div>
    """
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🧠 Deep Agent")

    st.caption(
        "AI-powered research, web extraction, "
        "report generation and quality analysis."
    )

    st.divider()

    st.markdown("### ⚡ Agents")

    st.markdown(
        """
        🔎 **Search Agent**  
        Tavily Web Search

        📄 **Reader Agent**  
        BeautifulSoup

        ✍️ **Writer Chain**  
        LLM + Structured Output

        🧐 **Critic Chain**  
        LLM + Structured Output
        """
    )

    st.divider()

    st.markdown("### 🛠️ Stack")

    st.caption("LangChain")
    st.caption("Tavily")
    st.caption("BeautifulSoup")
    st.caption("LLM")
    st.caption("Structured Output Parser")
    st.caption("Streamlit")


# ============================================================
# MAIN COLUMNS
# ============================================================

left, right = st.columns(
    [3.5, 1.5],
    gap="large"
)


# ============================================================
# LEFT SIDE
# ============================================================

with left:

    st.html(
        """
        <div class="research-box">

            <div class="research-title">
                🔬 Start a Research Task
            </div>

            <div class="research-description">
                Enter a topic and Deep Agent will search the web,
                extract relevant information, generate a report,
                and critically review the result.
            </div>

        </div>
        """
    )

    topic = st.text_area(
        "Research Topic",
        placeholder=(
            "Example: What are the major reasons behind "
            "the increase in petrol prices in India?"
        ),
        height=120,
        label_visibility="collapsed",
    )

    research_button = st.button(
        "🚀  Start Deep Research",
        type="primary",
        use_container_width=True,
    )


    # ========================================================
    # RUN PIPELINE
    # ========================================================

    if research_button:

        if not topic.strip():

            st.warning(
                "Please enter a research topic."
            )

        else:

            st.session_state["topic"] = topic

            progress = st.progress(0)

            status = st.empty()

            try:

                status.info(
                    "🔎 Deep Agent is researching..."
                )

                progress.progress(15)

                # YOUR EXISTING PIPELINE
                state = run_research_pipeline(topic)

                progress.progress(100)

                status.success(
                    "✅ Research completed successfully."
                )

                st.session_state["research_state"] = state

            except Exception as e:

                progress.empty()

                st.error(
                    f"❌ Pipeline error: {str(e)}"
                )

                st.stop()


    # ========================================================
    # RESULTS
    # ========================================================

    if "research_state" in st.session_state:

        state = st.session_state["research_state"]

        st.markdown(
            '<div class="result-title">📊 Research Intelligence</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="result-topic">
                Topic: {st.session_state.get("topic", "")}
            </div>
            """,
            unsafe_allow_html=True,
        )

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "🔎 Search Results",
                "📄 Scraped Content",
                "📝 Final Report",
                "🧐 Critic Feedback",
            ]
        )


        # ----------------------------------------------------
        # SEARCH
        # ----------------------------------------------------

        with tab1:

            st.subheader("Tavily Search Results")

            st.write(
                state.get(
                    "search_results",
                    "No search results available."
                )
            )


        # ----------------------------------------------------
        # SCRAPED
        # ----------------------------------------------------

        with tab2:

            st.subheader(
                "BeautifulSoup Scraped Content"
            )

            st.write(
                state.get(
                    "scraped_content",
                    "No scraped content available."
                )
            )


        # ----------------------------------------------------
        # REPORT
        # ----------------------------------------------------

        with tab3:

            st.subheader(
                "Final Research Report"
            )

            report = state.get(
                "report",
                "No report generated."
            )

            st.write(report)

            st.download_button(
                "📥 Download Report",
                data=str(report),
                file_name="deep_agent_report.txt",
                mime="text/plain",
                use_container_width=True,
            )


        # ----------------------------------------------------
        # CRITIC
        # ----------------------------------------------------

        with tab4:

            st.subheader(
                "Critic Analysis & Feedback"
            )

            st.write(
                state.get(
                    "feedback",
                    "No critic feedback available."
                )
            )


    else:

        st.html(
            """
            <div style="
                text-align:center;
                padding:70px 20px;
            ">

                <div style="
                    font-size:50px;
                    margin-bottom:12px;
                ">
                    🧠
                </div>

                <div style="
                    color:#ffffff;
                    font-size:21px;
                    font-weight:700;
                ">
                    Deep Agent is Ready
                </div>

                <div style="
                    color:#717b88;
                    font-size:13px;
                    max-width:550px;
                    margin:8px auto;
                    line-height:1.6;
                ">
                    Enter a research topic and let Deep Agent
                    coordinate search, extraction, writing and
                    critical analysis.
                </div>

            </div>
            """
        )


# ============================================================
# RIGHT SIDE — PIPELINE
# ============================================================

with right:

    st.html(
        """
        <div class="pipeline-wrapper">

            <div class="pipeline-heading">

                <div class="pipeline-heading-text">
                    ⚡ Live Pipeline
                </div>

                <div class="ready-badge">
                    ● READY
                </div>

            </div>


            <!-- SEARCH -->

            <div class="agent-card">

                <div class="agent-icon">
                    🔎
                </div>

                <div>
                    <div class="agent-name">
                        Search Agent
                    </div>

                    <div class="agent-tool">
                        Tavily
                    </div>
                </div>

                <div class="agent-number">
                    01
                </div>

            </div>


            <div class="pipeline-line"></div>


            <!-- READER -->

            <div class="agent-card">

                <div class="agent-icon">
                    📄
                </div>

                <div>
                    <div class="agent-name">
                        Reader Agent
                    </div>

                    <div class="agent-tool">
                        BeautifulSoup
                    </div>
                </div>

                <div class="agent-number">
                    02
                </div>

            </div>


            <div class="pipeline-line"></div>


            <!-- WRITER -->

            <div class="agent-card">

                <div class="agent-icon">
                    ✍️
                </div>

                <div>
                    <div class="agent-name">
                        Writer Chain
                    </div>

                    <div class="agent-tool">
                        LLM + Parser
                    </div>
                </div>

                <div class="agent-number">
                    03
                </div>

            </div>


            <div class="pipeline-line"></div>


            <!-- CRITIC -->

            <div class="agent-card">

                <div class="agent-icon">
                    🧐
                </div>

                <div>
                    <div class="agent-name">
                        Critic Chain
                    </div>

                    <div class="agent-tool">
                        LLM + Parser
                    </div>
                </div>

                <div class="agent-number">
                    04
                </div>

            </div>

        </div>
        """
    )


    # ========================================================
    # ARCHITECTURE CARD
    # ========================================================

    st.html(
        """
        <div class="architecture">

            <div class="architecture-title">
                🏗️ Agent Architecture
            </div>

            <div class="architecture-flow">

                User Query
                <br>
                ↓
                <br>

                <span>Tavily Search</span>
                <br>
                ↓
                <br>

                <span>BeautifulSoup</span>
                <br>
                ↓
                <br>

                <span>Writer Chain</span>
                <br>
                ↓
                <br>

                <span>Critic Chain</span>
                <br>
                ↓
                <br>

                Final Intelligence

            </div>

        </div>
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="footer">
        Deep Agent · Multi-Agent Research Intelligence
        <br>
        Tavily • BeautifulSoup • LangChain • LLM
    </div>
    """
)