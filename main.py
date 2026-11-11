#!/usr/bin/env python3
"""Write the best summary of 11 November 2026 world news (make.fun news-summary-01).

Writes one summary, in English (1,968 characters, within the 1-2,000 limit),
to argv[1] (default $MAKEFUN_OUTPUT_DIR/entry.txt or /output/entry.txt).
Python 3.13 standard library only, no network, fully deterministic: the same
summary bytes on every run.
"""

import os
import sys

# Nine stories, ordered by importance: Abu Dhabi prisoner exchange, COP31,
# Strait of Hormuz tankers, DOJ/Bessent, DRC Ebola, Israel's Knesset,
# Hegseth impeachment vote, the UK spy arrest, and US inflation.
SUMMARY = """World news, Wednesday 11 November 2026. Russia and Ukraine agreed a large prisoner exchange as two days of US-mediated talks ended in Abu Dhabi; President Zelenskyy called the talks 'constructive and quite substantive,' and US envoy Jared Kushner called the swap the biggest humanitarian release, with 1,000 to 1,500 prisoners per side under discussion (BBC). World leaders opened the COP31 climate summit in Antalya, Turkey, where 102 heads of state gathered; UN chief Antonio Guterres warned the climate crisis is 'outrunning us,' while the United States stayed away for a second year (AFP). In the Strait of Hormuz, three oil tankers caught fire after striking naval mines, among at least 37 attacks on ships there in November, as US Secretary of State Marco Rubio said there was 'really no need for major combat operations any longer' (Reuters). The US Justice Department charged three Iran-backed operatives over nearly 20 plots in the United States and Europe, including a September plot at RAF Fairford in England, and Treasury Secretary Scott Bessent was moved to a military base after threats to his life (BBC). The Ebola outbreak in the Democratic Republic of Congo passed 11,042 cases and 5,387 deaths, the second-largest and second-deadliest on record, with no licensed vaccine for the Bundibugyo strain (Reuters). Israel swore in a new parliament with no government after an election stripped Benjamin Netanyahu of his majority, leaving Gadi Eisenkot to try to build a coalition (AP). In Washington, the House voted 211-204 to send the effort to impeach Defense Secretary Pete Hegseth to committee, effectively ending it, and Republicans elected Jim Jordan as minority leader (AP). British police arrested a 41-year-old US Army officer serving with a NATO unit in Gloucestershire on suspicion of spying for Russia (BBC). US consumer prices rose 0.4% in October, above the 0.3% forecast, making a December Federal Reserve rate rise look near-certain (BLS)."""


def main():
    # Output path: first CLI argument, else $MAKEFUN_OUTPUT_DIR/entry.txt,
    # else /output/entry.txt. The summary is 1,968 characters (limit 1-2,000).
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
    )
    with open(out, "w", encoding="utf-8") as f:
        f.write(SUMMARY)
    print("wrote %s (%d characters)" % (out, len(SUMMARY)))


if __name__ == "__main__":
    main()
