(() => {
	const dark_theme = "/static/css/dark-theme.css";
	const light_theme = "/static/css/light-theme.css";

	const set_theme = (theme) => {
		$(".theme").remove();

		$("head").append(
			`<link rel="stylesheet" href="${theme}" class="theme">`
		);
	};

	const next_theme = (theme) => {
		if (theme == light_theme)
			return dark_theme;
		return light_theme;
	};

	const get_curr_theme = () => {
		return localStorage.getItem("theme") || light_theme;
	};

	const set_curr_theme = (theme) => {
		localStorage.setItem("theme", theme)
	}

	const change_theme = () => {
		let t = get_curr_theme();
		t = next_theme(t);
		set_curr_theme(t);
		set_theme(t);
	};

	$(".change-theme").click(change_theme);
	set_theme(get_curr_theme());
})();