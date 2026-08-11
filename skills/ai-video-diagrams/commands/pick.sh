#!/usr/bin/env bash
# pick — choose the right diagram type for a client request.
# Usage: ./commands/pick.sh "<what the client needs to understand>"
set -u
case "${1:-}" in
  *pipeline*|*flow*|*stage*) echo "pipeline — assets/example-pipeline.html";;
  *model*|*pick*|*choose*|*which*) echo "decision tree — assets/example-decision-tree.html";;
  *character*|*persona*|*who*) echo "character sheet — assets/example-character-sheet.html";;
  *look*|*feel*|*style*|*palette*) echo "style board — assets/example-style-board.html";;
  *who does*|*role*|*handoff*) echo "swimlane — assets/example-swimlane.html";;
  *exchange*|*api*|*call*|*request*) echo "sequence — assets/example-sequence.html";;
  *position*|*compare*|*cost*) echo "quadrant — assets/example-quadrant.html";;
  *stack*|*layer*|*on top*) echo "layers — assets/example-layers.html";;
  *lifecycle*|*status*|*state*|*approv*) echo "state — assets/example-state.html";;
  *loop*|*cycle*|*flywheel*) echo "loop — assets/example-loop.html";;
  *architect*|*system*|*setup*) echo "architecture — assets/example-architecture.html";;
  *schedule*|*week*|*plan*) echo "timeline — assets/example-timeline.html";;
  *break*|*folder*|*structure*) echo "tree — assets/example-tree.html";;
  *funnel*|*shortlist*|*narrow*) echo "funnel — assets/example-funnel.html";;
  *) echo "No confident match. Ask the client one question: single stage, or the whole story?";;
esac