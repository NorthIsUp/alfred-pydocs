//! An Alfred Script Filter. The menu, routes and integrations live in `workflow/workflow.toml`;
//! add Rust behavior with `.feature(…)`, `.keyword(…)` or `.provider(…)` on the [`Workflow`].

use we_love_alfred::Workflow;

#[tokio::main(flavor = "current_thread")]
async fn main() -> we_love_alfred::Result<()> {
    // Alfred runs scripts in the workflow folder; background refreshes inherit it.
    Workflow::load("workflow.toml")
        .await?
        .run(std::env::args().skip(1))
        .await
}

#[cfg(test)]
mod tests {
    use we_love_alfred::Config;

    #[test]
    fn workflow_toml_parses() {
        let parsed = include_str!("../workflow/workflow.toml").parse::<Config>();
        assert!(parsed.is_ok(), "{parsed:?}");
    }
}
