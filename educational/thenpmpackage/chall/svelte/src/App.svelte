<script>
	import '@kahi-ui/framework/dist/kahi-ui.framework.css';
	import { Offscreen, Spacer, Text, Box, Stack, Grid, Button, TextInput } from '@kahi-ui/framework';
	let dirtyJson;
	let cleanJson;
	let errors = '';

	let promise = getBeautifulJSON();

	function isJsonString(str) {
    try {
        JSON.parse(str);
    } catch (e) {
        return false;
    }
    return true;
}

	async function getBeautifulJSON() {
		const rawResponse = await fetch('/wash', {
			method: 'POST',
			body: dirtyJson,
			headers: {
				'Content-type': 'application/json',
				Connection: 'keep-alive'
			}
		});
		if (rawResponse.ok) {
			return await rawResponse.text();
		} else {
			return await (await rawResponse.text()).replace('\\n', '<br/>');
		}
	}

	function klikk() {
		promise = getBeautifulJSON();
		promise.then((res) => {
			console.dir(res);
			if (isJsonString(res)) {
				errors = '';
				cleanJson = JSON.stringify(JSON.parse(res),null,2);
			} else {
				errors = res;
				cleanJson = '❌';
			}
		}).catch((res, e) => {
			errors = res;
			cleanJson = '❌';			
		});;
	}
</script>

<Stack alignment_y="bottom">
	<Box palette="dark" padding_x="medium" padding_y="tiny">
		<Stack orientation="horizontal" spacing="small" alignment_y="bottom">
			INPUT
			<Spacer />
			<Button
				style="padding: 0px 7px 0px;"
				palette="light"
				size="tiny"
				variation="outline"
				for="offscreen-preview"
			>
				<Text size="huge" is="strong">JSON FORMATTER</Text>
			</Button>
			<Spacer />
			OUTPUT
		</Stack>
	</Box>
	<Box padding="small">
		<Grid.Container class="grid-item-span" points={['4', 'mobile:1']} spacing="small">
			<Grid.Item span_x="2">
				<TextInput
					palette="dark"
					is="textarea"
					bind:value={dirtyJson}
					placeholder="Paste JSON here..."
					resizable
				/>
			</Grid.Item><Grid.Item span_x="2">
				<TextInput
					height="prose"
					is="textarea"
					bind:value={cleanJson}
					resizable
					readonly
				/></Grid.Item
			>
			<Grid.Item span_x="2"
				><Button palette="accent" on:click={klikk}>
					<Text is="span">&lcub; &rcub;</Text></Button
				></Grid.Item
			>

			<Grid.Item span_x="2">
				<Text palette="negative">
					{@html errors}
				</Text>
			</Grid.Item>
		</Grid.Container>
	</Box>
</Stack>
<Box palette="dark" padding="tiny">
	<Stack orientation="horizontal" alignment_y="center" alignment_x="center" spacing="small">
		<b>powered by </b>
		<i> <a href="https://www.npmjs.com/package/node-serialize/v/0.0.4">node-serialize v0.0.4 </a></i>
	</Stack>
</Box>
